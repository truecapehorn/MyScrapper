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

def price_preparation(price):
    price_number = re.sub("[\n\t\s]*", "", price)  # usuniecie bialych znakow
    price_number = re.sub(",", ".", price_number)
    price_number = re.split("[zpPZUuEe]", price_number)[0]
    return float(price_number)


def parase(url,container,selectors,selec_name):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0'}

    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        price = soup.find(container, {selectors: selec_name})
        price_number = price_preparation(price.text)
        return print(f"Cena w {url}: - {price_number} zł")

    except Exception as e:
        print(url, e)


url1 = 'https://cumulus.equipment/pl_pl/spiwory/quilty-komfortery.html'
url2 = 'https://kross.eu/pl/rowery/szosowe/gravel/esker-4-0-zielony-czarny-polysk'
url3 = 'https://www.merida-bikes.com/pl-pl/bike/667/silex-400'



parase(url1,"span","id","product-price-78")
parase(url2,"div","class","a-price")
parase(url3,"span","class","price")


test=price_preparation("1234,85")
print(test)