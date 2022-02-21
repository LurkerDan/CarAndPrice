from bs4 import BeautifulSoup
from Analyzer import Analyzer
from GoogleSheet import GoogleSheet
import requests

analyzer = Analyzer()
gsheet = GoogleSheet()

page = 0

arr_cars = []
arr_prices = []
while page!=3:
    page += 1

    response = requests.get('https://kolesa.kz/cars/?page=' + str(page))
    html = BeautifulSoup(response.content, 'html.parser')

    prices = html.find_all('span', class_='price')
    cars = html.select('div > div.a-info-top')

    pages = str(html.find_all('div', class_='finded'))
    total_pages = analyzer.find_int(pages)

    for i in cars:
        car = i.select('span.a-el-info-title > a')
        arr_cars.append(car[0].text)
        total_cars = analyzer.delete_space(arr_cars)

    for i in range(20):
        arr_prices.append(prices[i].text)
        total_prices = analyzer.delete_sings(arr_prices)

print(total_prices)
print(total_cars)
total = list(zip(total_prices,total_cars))

print(total)