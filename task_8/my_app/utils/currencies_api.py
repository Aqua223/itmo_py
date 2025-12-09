import requests
import datetime
import xml.etree.ElementTree as ET

from task_8.my_app.models import Currency


def get_currencies(url: str = 'https://www.cbr-xml-daily.ru/daily_json.js') -> list:
    """ Парсер, который извлекает информацию о валютах по данным центробанка РФ

    Обрабатывает url с учетом недоступности API, некорректности JSON-файла и отсутствия ключа "Valute"
    в исходных данных. Возвращает список Currency-объектов.

    :param url: ссылка, из которой парсится информация о валютах
    :return: список из Currency объектов
    :rtype: list[Currency]
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"API is unavailable: {e}")

    try:
        data = response.json()
    except ValueError as e:
        raise ValueError(f"Некорректный JSON: {e}")

    if "Valute" not in response.json():
        raise KeyError("Key 'Valute' not found")

    currencies = []

    for currency in data["Valute"].values():
        currencies.append(
            Currency(
                id=currency["ID"],
                num_code=currency["NumCode"],
                char_code=currency["CharCode"],
                nominal=currency["Nominal"],
                name=currency["Name"],
                value=currency["Value"]
            )
        )

    return currencies


def get_currency_history(currency_id: str, days: int = 90) -> list:
    """ Парсер, который получает исторические данные курса валюты по данным Центробанка РФ.

    Формирует запрос к API ЦБ РФ, загружает XML с историей за указанный период,
    обрабатывает ошибки сети и некорректный XML. Возвращает список словарей
    с датой и значением валюты.

    :param currency_id: ID валюты по классификатору ЦБ РФ
    :param days: количество дней, за которые нужно получить историю (по умолчанию 90)
    :return: список словрей вида {"date": str, "value": float}
    :rtype: list[dict]
    """

    date_to = datetime.date.today()
    date_from = date_to - datetime.timedelta(days=days)

    url = (
        f"https://www.cbr.ru/scripts/XML_dynamic.asp?"
        f"date_req1={date_from.strftime('%d/%m/%Y')}"
        f"&date_req2={date_to.strftime('%d/%m/%Y')}"
        f"&VAL_NM_RQ={currency_id}"
    )

    response = requests.get(url)
    response.raise_for_status()

    try:
        data = ET.fromstring(response.content)
    except Exception:
        raise ValueError("Некорректный XML от ЦБ РФ")

    result = []

    for record in data.findall("Record"):
        date = record.attrib["Date"]
        value_str = record.find("Value").text.replace(",", ".")
        value = float(value_str)

        result.append({
            "date": date,
            "value": value
        })

    return result
