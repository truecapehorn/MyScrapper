import requests
from bs4 import BeautifulSoup
import re
import yagmail
import os

email = os.environ.get('EMAIL_USER2')
password = os.environ.get("EMAIL_PASSWORD2")

def send_email(body):
    receiver = 'jablonski.norbert@gmail.com'
    try:

        yag = yagmail.SMTP(user=email,password=password)
        yag.send(to=receiver, subject="Alert cenowy", contents=body, )
        print("Mail wysłany")
    except Exception as e:
        print("Problem z wyslaniem meila: {}".format(e))



def check_price(prices):
    body=""
    for k,v in prices.items():
        b=f"url= {v['url']} , cena = {v['price']} zł.\n"
        body=body+b
    print(body)

    # send_email(body)




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
        return price_number

    except Exception as e:
        print(url, e)


url1 = 'https://cumulus.equipment/pl_pl/spiwory/quilty-komfortery.html'
url2 = 'https://kross.eu/pl/rowery/szosowe/gravel/esker-4-0-zielony-czarny-polysk'
url3 = 'https://www.merida-bikes.com/pl-pl/bike/667/silex-400'
url4 = 'https://rower.com.pl/merida-silex-400--2079478'
url5 = 'http://www.megastart.pl/rowery/turystyczne/silex/107-silex-400'



cena1=parase(url1,"span","id","product-price-78")
cena2=parase(url2,"div","class","a-price")
cena3=parase(url3,"span","class","price")
cena4=parase(url4,"span","class","base-price")
cena5=parase(url5,"span","class","price")

dane={
    "cena1":{"price":cena1,"url":url1},
    "cena2":{"price":cena2,"url":url2},
    "cena3":{"price":cena3,"url":url3},
    "cena4":{"price":cena4,"url":url4},
    "cena5":{"price":cena5,"url":url5},
      }
check_price(dane)