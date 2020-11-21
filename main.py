import requests
from bs4 import BeautifulSoup
import re


def send_email(body):
    import yagmail

    receiver = "tito02@o2.pl"
    try:
        yag = yagmail.SMTP("jablonski.norbert@gmail.com")
        yag.send(to=receiver, subject="Cena TV Boxa", contents=body, )
        print("Mail wysłany")
    except Exception as e:
        print("Problem z wyslaniem meila: {}".format(e))


def check_price(price_float):
    if price_float < 350:
        email = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        <h2>Paraser wykryl ze cena tv boxa jest optymalna:</h2>
        <h3>Jego cena to <b>{} zl</b></h3>.
    </body>
    </html>""".format(price_float)
        print(email)
        send_email(email)


# check_price(price_float)

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

url1 = 'https://cumulus.equipment/pl_pl/spiwory/quilty-komfortery.html'
url2 = 'https://kross.eu/pl/rowery/szosowe/gravel/esker-4-0-zielony-czarny-polysk'
url3 = 'https://www.merida-bikes.com/pl-pl/bike/667/silex-400'

for url in [url1, url2, url3]:
    try:
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        if url == url1:
            price = soup.find("span", {"id": "product-price-78"})
        elif url == url2:
            price = soup.find("div", {"class": 'a-price'})
        elif url == url3:
            price = soup.find("span", {"class": 'price'})

        price_number = re.sub("[\n\t\s]+", "", price.text)  # usuniecie bialych znakow
        price_number = price_number.replace(",", ".").split("z")[0]    # tylko cena
        print(f"Cena w {url}: - {float(price_number)} zł")

    except Exception as e:
        print(url, e)
