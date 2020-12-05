import requests
from bs4 import BeautifulSoup
import re
import json
import datetime


def parase(url, container, selectors, selec_name):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find(container, {selectors: selec_name})
        price_number = price_preparation(price.text)
        return price_number

    except Exception as e:
        print(url, e)


def price_preparation(price):
    price_number = re.sub("[\n\t\s]*", "", price)  # usuniecie bialych znakow
    price_number = re.sub(",", ".", price_number)
    price_number = re.split("[zpPZUuEe]", price_number)[0]
    return float(price_number)


with open('data.json') as f:
    data = json.load(f)
dane = []

# now = datetime.date.today()
now = datetime.datetime.now()


for k, v in data.items():
    cena = parase(v['url'], v['container'], v['selectors'], v['selec_name'])
    dane.append({"name": k, "price": cena, "url": v['url'], "currency": v['currency'], "date": now})

if __name__ == "__main__":
    print(now, len(dane))
    for i in dane:
        print(i)
