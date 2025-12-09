import unittest
import requests
import http.client

from unittest.mock import patch, MagicMock
from models import Author, App, Currency, User, UserCurrency
from utils.currencies_api import get_currencies

from myapp import index_content, author_content, currencies_content, users_content
from myapp import currencies


class TestAuthor(unittest.TestCase):
    """ Тестирует модель Author """
    # name
    def test_incorrect_name(self):
        with self.assertRaises(ValueError):
            Author("")

    def test_name_setter(self):
        a = Author("Ryan")
        a.name = "Bob"
        self.assertEqual(a.name, "Bob")

    def test_name_setter_invalid(self):
        a = Author("Ryan")
        with self.assertRaises(ValueError):
            a.name = ""

    # group
    def test_incorrect_group(self):
        with self.assertRaises(ValueError):
            Author("Michael", "H243")

    def test_group_setter(self):
        a = Author("Ryan")
        a.group = "Р3120"
        self.assertEqual(a.group, "Р3120")

    def test_group_setter_invalid(self):
        a = Author("Ryan")
        with self.assertRaises(ValueError):
            a.group = ""


class TestApp(unittest.TestCase):
    """ Тестирует модель App """
    # name
    def test_incorrect_name(self):
        with self.assertRaises(ValueError):
            App("", "2", Author("Nikita"))

    def test_name_setter(self):
        a = App("Gleb", "2", Author("Nikita"))
        a.name = "Bob"
        self.assertEqual(a.name, "Bob")

    def test_name_setter_invalid(self):
        a = App("Gleb", "2", Author("Nikita"))
        with self.assertRaises(ValueError):
            a.name = ""

    # version
    def test_incorrect_version(self):
        with self.assertRaises(ValueError):
            App("Gleb", "", Author("Nikita"))

    def test_version_setter(self):
        a = App("Gleb", "2", Author("Nikita"))
        a.version = "1"
        self.assertEqual(a.version, "1")

    def test_version_setter_invalid(self):
        a = App("Gleb", "2", Author("Nikita"))
        with self.assertRaises(ValueError):
            a.version = ""

    # author
    def test_incorrect_author(self):
        with self.assertRaises(ValueError):
            App("Gleb", "", "skibidipapa")

    def test_author_setter(self):
        a = App("Gleb", "2", Author("Nikita"))
        new_author = Author("Gleb")
        a.author = new_author
        self.assertEqual(a.author, new_author)

    def test_author_setter_invalid(self):
        a = App("Gleb", "2", Author("Nikita"))
        with self.assertRaises(ValueError):
            a.author = "ITMO"


class TestCurrency(unittest.TestCase):
    """ Тестирует модель Currency """
    # id
    def test_incorrect_id(self):
        with self.assertRaises(ValueError):
            Currency("", "840", "USD", "Dollar", 90.12, 1)

    def test_id_setter(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        c.id = "R01239"
        self.assertEqual(c.id, "R01239")

    def test_id_setter_invalid(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        with self.assertRaises(ValueError):
            c.id = ""

    # num_code
    def test_incorrect_num_code(self):
        with self.assertRaises(ValueError):
            Currency("R01235", "", "USD", "Dollar", 90.12, 1)

    def test_num_code_setter(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        c.num_code = "978"
        self.assertEqual(c.num_code, "978")

    def test_num_code_setter_invalid(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        with self.assertRaises(ValueError):
            c.num_code = ""

    # char_code
    def test_incorrect_char_code(self):
        with self.assertRaises(ValueError):
            Currency("R01235", "840", "", "Dollar", 90.12, 1)

    def test_char_code_setter(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        c.char_code = "EUR"
        self.assertEqual(c.char_code, "EUR")

    def test_char_code_setter_invalid(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        with self.assertRaises(ValueError):
            c.char_code = ""

    # name
    def test_incorrect_name(self):
        with self.assertRaises(ValueError):
            Currency("R01235", "840", "USD", "", 90.12, 1)

    def test_name_setter(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        c.name = "Euro"
        self.assertEqual(c.name, "Euro")

    def test_name_setter_invalid(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        with self.assertRaises(ValueError):
            c.name = ""

    # value
    def test_incorrect_value(self):
        with self.assertRaises(ValueError):
            Currency("R01235", "840", "USD", "Dollar", -1, 1)

    def test_value_setter(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        c.value = 100.5
        self.assertEqual(c.value, 100.5)

    def test_value_setter_invalid(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        with self.assertRaises(ValueError):
            c.value = -10

    # nominal
    def test_incorrect_nominal(self):
        with self.assertRaises(ValueError):
            Currency("R01235", "840", "USD", "Dollar", 90.12, 0)

    def test_nominal_setter(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        c.nominal = 10
        self.assertEqual(c.nominal, 10)

    def test_nominal_setter_invalid(self):
        c = Currency("R01235", "840", "USD", "Dollar", 90.12, 1)
        with self.assertRaises(ValueError):
            c.nominal = 0


class TestUser(unittest.TestCase):
    """ Тестирует модель User """
    # id
    def test_incorrect_id(self):
        with self.assertRaises(ValueError):
            User("", "Bob")

    def test_id_setter(self):
        u = User("1", "Bob")
        u.id = "2"
        self.assertEqual(u.id, "2")

    def test_id_setter_invalid_value(self):
        u = User("1", "Bob")
        with self.assertRaises(ValueError):
            u.id = ""

    # -------- name --------
    def test_incorrect_name(self):
        with self.assertRaises(ValueError):
            User("1", "")

    def test_name_setter(self):
        u = User("1", "Alice")
        u.name = "Bob"
        self.assertEqual(u.name, "Bob")

    def test_name_setter_invalid_value(self):
        u = User("1", "Alice")
        with self.assertRaises(ValueError):
            u.name = ""


class TestUserCurrency(unittest.TestCase):
    """ Тестирует модель UserCurrency """
    # id
    def test_incorrect_id(self):
        with self.assertRaises(ValueError):
            UserCurrency("", "1", "USD")

    def test_id_setter(self):
        uc = UserCurrency("10", "1", "USD")
        uc.id = "20"
        self.assertEqual(uc.id, "20")

    def test_id_setter_invalid(self):
        uc = UserCurrency("10", "1", "USD")
        with self.assertRaises(ValueError):
            uc.id = ""

    # user_id
    def test_incorrect_user_id(self):
        with self.assertRaises(ValueError):
            UserCurrency("10", "", "USD")

    def test_user_id_setter(self):
        uc = UserCurrency("10", "1", "USD")
        uc.user_id = "999"
        self.assertEqual(uc.user_id, "999")

    def test_user_id_setter_invalid(self):
        uc = UserCurrency("10", "1", "USD")
        with self.assertRaises(ValueError):
            uc.user_id = ""

    # currency_id
    def test_incorrect_currency_id(self):
        with self.assertRaises(ValueError):
            UserCurrency("10", "1", "")

    def test_currency_id_setter(self):
        uc = UserCurrency("10", "1", "USD")
        uc.currency_id = "EUR"
        self.assertEqual(uc.currency_id, "EUR")

    def test_currency_id_setter_invalid(self):
        uc = UserCurrency("10", "1", "USD")
        with self.assertRaises(ValueError):
            uc.currency_id = ""


class TestGetCurrencies(unittest.TestCase):
    """ Тестирует функцию get_currencies"""
    # Ошибка сети
    @patch("utils.currencies_api.requests.get")
    def test_get_currencies_network_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network error")

        with self.assertRaises(ConnectionError):
            get_currencies()

    # Некорректный JSON
    @patch("utils.currencies_api.requests.get")
    def test_get_currencies_invalid_json(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError("Invalid JSON")  # имитируем плохой JSON
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError):
            get_currencies()

    # Нет ключа Valute
    @patch("utils.currencies_api.requests.get")
    def test_get_currencies_missing_valute(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {}  # нет ключа "Valute"
        mock_get.return_value = mock_response

        with self.assertRaises(KeyError):
            get_currencies()

    # Проверка корректного парсинга полей
    @patch("utils.currencies_api.requests.get")
    def test_currency_fields_parsed_correctly(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "Valute": {
                "EUR": {
                    "ID": "R01239",
                    "NumCode": "978",
                    "CharCode": "EUR",
                    "Nominal": 1,
                    "Name": "Евро",
                    "Value": 100.55
                }
            }
        }
        mock_get.return_value = mock_response

        result = get_currencies()
        eur = result[0]

        self.assertEqual(eur.id, "R01239")
        self.assertEqual(eur.num_code, "978")
        self.assertEqual(eur.char_code, "EUR")
        self.assertEqual(eur.nominal, 1)
        self.assertEqual(eur.name, "Евро")
        self.assertEqual(eur.value, 100.55)


class TestSimpleHTTPRequestHandler(unittest.TestCase):
    """ Тестирует контроллер """
    # /
    def test_root(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/")
        response = conn.getresponse()
        html = response.read().decode()

        self.assertEqual(response.status, 200)
        self.assertIn("Добро", html)

    # /users
    def test_users(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/users")
        response = conn.getresponse()
        html = response.read().decode()

        self.assertEqual(response.status, 200)
        self.assertIn("Список пользователей", html)

    # /currencies
    def test_currencies(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/currencies")
        response = conn.getresponse()
        html = response.read().decode()

        self.assertEqual(response.status, 200)
        self.assertIn("AUD", html)

    # /author
    def test_author(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/author")
        response = conn.getresponse()
        html = response.read().decode()

        self.assertEqual(response.status, 200)
        self.assertIn("Ryan Gosling", html)

    # /user?id=1
    def test_user_valid(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/user?id=1")
        response = conn.getresponse()
        html = response.read().decode()

        self.assertEqual(response.status, 200)
        self.assertIn("Jason Statham", html)

    # /user
    def test_user_without_id(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/user")

        response = conn.getresponse()

        self.assertEqual(response.status, 400)

    # /user?id=999
    def test_user_not_found(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/user?id=999")
        response = conn.getresponse()

        self.assertEqual(response.status, 404)

    # неизвестный путь
    def test_not_found_route(self):
        conn = http.client.HTTPConnection("localhost", 8080)
        conn.request("GET", "/unknown")
        response = conn.getresponse()

        self.assertEqual(response.status, 404)


class TestTemplates(unittest.TestCase):
    """ Тестирует шаблоны """
    def test_index_content(self):
        html = index_content

        self.assertIn('<a href="/">Основная страница</a>', html)
        self.assertIn('<a href="/users">Список пользователей</a>', html)

    def test_author_content(self):
        html = author_content

        self.assertIn("Информация об авторе", html)

        self.assertIn("Ryan Gosling", html)
        self.assertIn("Р3123", html)

        self.assertIn("Имя:", html)
        self.assertIn("Группа:", html)

    def test_currencies_content(self):
        html = currencies_content

        for c in currencies:
            self.assertIn(c.id, html)
            self.assertIn(c.num_code, html)
            self.assertIn(c.char_code, html)
            self.assertIn(str(c.nominal), html)
            self.assertIn(c.name, html)
            self.assertIn(str(c.value), html)

    def test_users_content(self):
        html = users_content

        self.assertIn("Jason Statham", html)
        self.assertIn("Peter Parker", html)

        self.assertIn("id: 1", html)
        self.assertIn("id: 2", html)

        self.assertIn('/user?id=1', html)
        self.assertIn('/user?id=2', html)


if __name__ == "__main__":
    unittest.main()

