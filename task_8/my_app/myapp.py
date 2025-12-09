from jinja2 import Environment, PackageLoader, select_autoescape
from models import Author, App, User, UserCurrency
from utils.currencies_api import get_currencies, get_currency_history

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse

currencies = get_currencies()

CURRENCY_ID_MAP = {currency.char_code: currency.id for currency in currencies}
CURRENCY_CHAR_CODE_MAP = {currency.id: currency.char_code for currency in currencies}

main_author = Author('Ryan Gosling')
my_app = App(
    name="CurrenciesListApp",
    version="1.1",
    author=main_author
)

users = [
    {'id': '1', 'name': 'Jason Statham', 'subs': ['USD', 'EUR', 'AED']},
    {'id': '2', 'name': 'Magnus Carlsen', 'subs': ['CNY', 'TRY', 'OMR', 'RON', 'XDR']},
    {'id': '3', 'name': 'Peter Parker', 'subs': ['SGD', 'USD', 'UZS', 'CZK']}
]

users_processed = []
users_currencies = []
users_currencies_id = '1'

for user in users:
    user_obj = User(
        id=user['id'],
        name=user['name'],
    )

    for sub in user['subs']:
        user_currency_obj = UserCurrency(
            id=users_currencies_id,
            user_id=user['id'],
            currency_id=CURRENCY_ID_MAP[sub]
        )

        users_currencies.append(user_currency_obj)
        users_currencies_id = str(int(users_currencies_id) + 1)

    users_processed.append(user_obj)

env = Environment(
    loader=PackageLoader("myapp"),
    autoescape=select_autoescape()
)

template_index = env.get_template("index.html")
template_users = env.get_template("users.html")
template_currencies = env.get_template("currencies.html")
template_author = env.get_template("author.html")

index_content = template_index.render(my_app=my_app,
                      navigation=[{
                          'caption': 'Основная страница',
                          'href': "/"
                      }, {
                          'caption': 'Список пользователей',
                          'href': "/users"
                      }, {
                          'caption': 'Список валют',
                          'href': "/currencies"
                      }, {
                          'caption': 'Информация об авторе',
                          'href': "/author"
                      }],
                      author_name=main_author.name,
                      group=main_author.group
                      )
currencies_content = template_currencies.render(currencies=currencies)
author_content = template_author.render(main_author=main_author)
users_content = template_users.render(users=users_processed)


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """ Контроллер, который реализует маршрутизацию, обработку запросов, вызов моделей и шаблонов.

    Реализованные маршруты:
        GET /                – главная страница (index)
        GET /users           – список пользователей
        GET /user?id=<id>    – карточка пользователя, включая привязанные валюты
        GET /currencies      – список валют
        GET /author          – информация об авторе

    """
    def _send_html(self, html: str):
        """ Реализует успешный HTML-ответ клиенту.

        :param str html: Отрендеренный html-контент
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def _send_error(self, error: int, msg: bytes):
        """ Отправляет HTTP-ошибку клиенту, включая код статуса и текст сообщения.

        :param int error: Код ошибки
        :param bytes msg: Сообщение при ошибке
        """
        self.send_response(error)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(msg)

    def do_GET(self):
        """ Обработчик GET-запросов.

       Выполняет маршрутизацию по URL, извлекает query-параметры
       и передаёт данные в соответствующие шаблоны.

       Поддерживаемые маршруты:

       • "/" – возвращает главную страницу.
       • "/users" – возвращает HTML со списком пользователей.
       • "/user?id=<id>" – загружает данные конкретного пользователя и его валют.
           - Проверяет наличие параметра id.
           - Проверяет существование пользователя.
           - Генерирует графики по каждой валюте пользователя.
           - Передаёт данные в шаблон user.html.
       • "/currencies" – выводит список валют.
       • "/author" – выводит информацию об авторе.

       В случае неизвестного маршрута возвращается 404.
       """
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)

        if path == "/":
            return self._send_html(index_content)

        if path == "/users":
            return self._send_html(users_content)

        if path.startswith("/user"):
            if "id" not in params:
                self._send_error(400, b"Not Found")
                return

            uid = params["id"][0]
            user = next((u for u in users_processed if u.id == uid), None)
            user_currencies = [uc for uc in users_currencies if uc.user_id == uid]

            if user is None:
                self._send_error(404, b"User not found")
                return

            graphs = {}

            for uc in user_currencies:
                graphs[CURRENCY_CHAR_CODE_MAP[uc.currency_id]] = get_currency_history(uc.currency_id)

            template_user = env.get_template("user.html")
            user_content = template_user.render(
                user=user,
                graphs=graphs,
                user_currencies=user_currencies,
                map=CURRENCY_CHAR_CODE_MAP
            )

            return self._send_html(user_content)

        if path == "/currencies":
            return self._send_html(currencies_content)

        if path == "/author":
            return self._send_html(author_content)

        self._send_error(404, b"Page not found")


if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
    print('server is running')
    httpd.serve_forever()