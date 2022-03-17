import json
import requests
import re


URL_API = "https://www.cbr-xml-daily.ru/daily_json.js"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"}

full_page = requests.get(URL_API).json()  # получили json файл и привели его к словарю

with open("price", 'w') as f:
    json.dump(full_page, fp=f, sort_keys=True, indent=4)  # записали данные с сайта ЦБ в формате json в отдельный файл

nominal = float(full_page["Valute"]["USD"]["Nominal"])
value = float(full_page["Valute"]["USD"]["Value"])

date = full_page["Date"]
name_valute = full_page["Valute"]["USD"]["CharCode"]

pattern = re.search(r"(?P<Year>\d{4})-(?P<Month>\d{2})-(?P<Day>\d{2})T(?P<Time>.{8})(?P<GMT>.{6})", date)
result_date = pattern.groupdict()

day = result_date["Day"]
month = result_date["Month"]
year = result_date["Year"]
time = result_date["Time"]
GMT = result_date["GMT"]

print(f'Дата: {day}.{month}.{year} \nВремя: {time}({GMT}) \nКурс 1 {name_valute} = {round(value / nominal, 2)} руб')


