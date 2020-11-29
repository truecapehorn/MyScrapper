from data import dane
import yagmail
import os
from template import make_template
import pandas as pd

pd.set_option('display.width', None)
pd.set_option('colheader_justify', 'center')

email = os.environ.get('EMAIL_USER2')
password = os.environ.get("EMAIL_PASSWORD2")

if email == None or password == None:
    print(f"email:{email}; password:{password}")
    exit(0)


def send_email(body):
    receiver = 'jablonski.norbert@gmail.com'
    try:
        yag = yagmail.SMTP(user=email, password=password)
        yag.send(to=receiver, subject="Alert cenowy", contents=body, )
        print("Mail wysłany")
    except Exception as e:
        print("Problem z wyslaniem meila: {}".format(e))


def prepare_mail(prices):
    body = make_template(prices)
    return body


def write_to_file(content):
    with open('mail.html', 'w') as f:
        print(content, file=f)


df = pd.DataFrame(dane, columns=['date', 'name', 'url', 'price', 'currency'])
body = prepare_mail(df.to_html(classes='mystyle'))
write_to_file(body)
send_email(body)
print(df)
