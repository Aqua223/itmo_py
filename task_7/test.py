import unittest
import io
import logging
from unittest.mock import patch, MagicMock
import requests

from sol import get_currencies, logger

# Я использовал unittest.mock для того, чтобы создавать имитацию работы request.get, поскольку
# функция get_currencies зависит от requests.get (ведь информация о валютах непостоянна), поэтому
# для проверки работы функции мы имитируем requests.get и настраиваем под свои нужды


# Тестирование функции get_currencies
class TestGetCurrencies(unittest.TestCase):
    # Возврат реальных курсов
    @patch("sol.requests.get")
    def test_success(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "Valute": {
                "USD": {"Value": 76.2},
                "EUR": {"Value": 98.3}
            }
        }
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        result = get_currencies(["USD", "EUR"])

        self.assertEqual(result, {"USD": 76.2, "EUR": 98.3})

    # Несуществующая валюта
    @patch("sol.requests.get")
    def test_currency_not_found(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"Valute": {"USD": {"Value": 90.1}}}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        with self.assertRaises(KeyError):
            get_currencies(["RUB"])

    # Нет подключения
    @patch("sol.requests.get")
    def test_connection_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Network down")

        with self.assertRaises(ConnectionError):
            get_currencies(["USD"])

    # Некорректный JSON
    @patch("sol.requests.get")
    def test_invalid_json(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.raise_for_status.return_value = None
        mock_resp.json.side_effect = ValueError("Invalid JSON")

        mock_get.return_value = mock_resp

        with self.assertRaises(ValueError):
            get_currencies(["USD"])

    # Отсутствует ключ "Valute"
    @patch("sol.requests.get")
    def test_missing_valute_key(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"SomethingElse": {}}
        mock_resp.raise_for_status.return_value = None
        mock_get.return_value = mock_resp

        with self.assertRaises(KeyError):
            get_currencies(["USD"])


# Тестирование декоратора
class TestLoggerDecorator(unittest.TestCase):
    def setUp(self):
        self.stream = io.StringIO()

        @logger(handle=self.stream)
        def f(x):
            return x * 2

        @logger(handle=self.stream)
        def f_err(x):
            raise ValueError("error")

        self.f = f
        self.f_err = f_err

    # Успешное логирование
    def test_logger_success(self):
        result = self.f(5)
        logs = self.stream.getvalue()

        self.assertEqual(result, 10)

        self.assertRegex(logs, "INFO")
        self.assertRegex(logs, "Execute")
        self.assertRegex(logs, "Success")
        self.assertRegex(logs, "5")
        self.assertRegex(logs, "10")

    # Ошибка в логировании
    def test_logger_error(self):
        with self.assertRaises(ValueError):
            self.f_err(7)

        logs = self.stream.getvalue()

        self.assertRegex(logs, "ERROR")
        self.assertRegex(logs, "ValueError")
        self.assertRegex(logs, "error")


if __name__ == "__main__":
    unittest.main()
