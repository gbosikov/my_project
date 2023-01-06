from decimal import Decimal
import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    resp_text = response.text
    currency_idx = resp_text.find(code.upper())

    if currency_idx == -1:
        return
    else:
        resp_text = resp_text[currency_idx:resp_text.find('</Value>', currency_idx)]
        nominal = float(resp_text[resp_text.find('<Nominal>') + 9:resp_text.find('</Nominal>')].replace(',', '.'))
        value = float(resp_text[resp_text.find('<Value>') + 7:].replace(',', '.'))

    result_value = round(value / nominal, 2)
    return result_value


print(currency_rates("USD"))
print(currency_rates("noname"))

import csv
import requests
import xml.etree.ElementTree as ET





