import json
import requests
import re

from pprint import pprint


URL_API = "https://www.cbr-xml-daily.ru/daily_json.js"


def get_data(url) -> dict:
    """
    Функция, которая по ссылке получает JSON файл с данными курсов валют с сайта ЦБ РФ и сохраняет их в отдельный файл.
    Если интернет есть, то данные берутся с сайта, если отсутствует, то данные подгружаются из файла.
    :param url: ссылка на JSON файл, содержащий актуальные данные курсов валют, с сайта ЦБ
    :return: Словарь, содержащий данные курсов валют
    """
    try:
        full_page = requests.get(url).json()  # получили json файл и привели его к словарю
        with open("price", 'w') as f:
            json.dump(full_page, fp=f, sort_keys=True, indent=4)  # записали данные с сайта ЦБ в формате json в файл
    except OSError:
        with open("price", "r") as f:
            full_page = json.load(f)
    return full_page


data = get_data(URL_API)  # данные записали в переменную, которую будем использовать в другом файле
date = data["Date"]

pattern = re.search(r"(?P<Year>\d{4})-(?P<Month>\d{2})-(?P<Day>\d{2})T(?P<Time>.{8})(?P<GMT>.{6})", date)
result_date = pattern.groupdict()  # распарсили дату на отдельные данные и записали в словарь (день, месяц, год и т.д.)

day = result_date["Day"]
month = result_date["Month"]
year = result_date["Year"]
time = result_date["Time"]
GMT = result_date["GMT"]


if __name__ == '__main__':
    pprint(get_data(URL_API))
