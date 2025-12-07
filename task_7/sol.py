import sys
import functools
import requests
import io
import logging

from typing import Callable


def logger(func: Callable=None, *, handle=sys.stdout) -> Callable:
    """ Параметризуемый декоратор, который ведёт логирование в зависимости от аргумента handle

    :param func: декорируемая функция
    :param handle: поток вывода (куда будет произведено логирование)
    :return: возвращает задекорированную функцию
    :rtype: Callable
    """
    if func is None:
        return lambda func: logger(func, handle=handle)

    def log_info(message: str):
        """ Печатает сообщение message о выполнении кода с учётом потока handle (логирование)

        :param message: сообщение, которое печатается
        """
        if isinstance(handle, logging.Logger):
            handle.info(message)
        else:
            handle.write("INFO: " + message + "\n")

    def log_error(message: str):
        """ Печатает сообщение message об ошибке с учётом потока handle (логирование)

        :param message: сообщение, которое печатается
        """
        if isinstance(handle, logging.Logger):
            handle.error(message)
        else:
            handle.write("ERROR: " + message + "\n")

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        """ Функция обёртка

        Логируется сообщение о выполнении кода, дальше в зависимости от результата выполнения
        сообщается об успешном выполнении или выбрасывается исключение об ошибке
        """
        log_info(f"Execute: {func.__name__} args={args}, kwargs={kwargs}")

        try:
            result = func(*args, **kwargs)
            log_info(f"Success: {func.__name__} -> {result}")
            return result

        except Exception as e:
            log_error(f"Exception in {func.__name__}: {type(e).__name__}: {e}")
            raise e

    return wrapper


# настройка логгера
logging.basicConfig(
    filename="currency_file.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)

# куда будет логироваться информация
file_logger = logging.getLogger("currency_file")


@logger(handle=file_logger)
def get_currencies(currency_codes: list, url:str='https://www.cbr-xml-daily.ru/daily_json.js') -> dict:
    """
    Получает курсы валют с API Центробанка России.

    Args:
        currency_codes (list): Список символьных кодов валют (например, ['USD', 'EUR']).

    Returns:
        dict: Словарь, где ключи - символьные коды валют, а значения - их курсы.
              Возвращает None в случае ошибки запроса.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"API is unavailable: {e}")

    try:
        data = response.json()
    except ValueError as e:
        raise ValueError(f"Invalid JSON: {e}")

    currencies = {}

    if "Valute" not in data:
        raise KeyError(f'Key "Valute" not found')

    for code in currency_codes:
        if code not in data["Valute"]:
            raise KeyError(f'Code {code} is not found')

        value = data["Valute"][code]["Value"]

        if not isinstance(value, (int, float)):
            raise TypeError(f"Invalid type for currency {code}: {type(value)}")

        currencies[code] = value

    return currencies


# print(get_currencies(['XYZ', 'USD']))
