from bs4 import BeautifulSoup
from Analyzer import Analyzer
from GoogleSheet import GoogleSheet
import requests

analyzer = Analyzer()
gsheet = GoogleSheet()

page = 0

# Поиск общего кол-ва объявлений и деленние на кол-во объявлений на странице  дает общее количество страниц
response = requests.get('https://kolesa.kz/cars/?page=' + str(page))
html = BeautifulSoup(response.content, 'html.parser')
pages = str(html.find_all('div', class_='finded'))

total_pages = analyzer.find_int(pages)
print(f'Всего страниц на сайте {total_pages} \n Всего объявлений на сайте {total_pages *20}')
arr_cars = []
arr_prices = []

# Суммарное колличество обработки страниц
while page != 1:
    page += 1

    # Обращение к HTML странице
    response = requests.get('https://kolesa.kz/cars/?page=' + str(page))
    html = BeautifulSoup(response.content, 'html.parser')

    # Поиск Raw цен и машин на странице
    prices = html.find_all('span', class_='price')
    cars = html.select('div > div.a-info-top')

    # Цикл обработки массива машин с одной страницы
    for i in cars:
        car = i.select('span.a-el-info-title > a')
        arr_cars.append(car[0].text)
        total_cars = analyzer.delete_space(arr_cars)

    # Цикл обработки массива цен с одной страницы
    for i in range(20):
        arr_prices.append(prices[i].text)
        total_prices = analyzer.delete_sings(arr_prices)

# Упаковка массивов для отправки
total = list(zip(total_prices,total_cars))

# Отправка в гугл таблицы готового массива
gsheet.google_request(total)
