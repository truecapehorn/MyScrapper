from data import dane
import yagmail
import os
from template import make_template
import datetime
from pandas_operations import piv
now = datetime.date.today() # data do pliku

email = os.environ.get('EMAIL_USER2')
password = os.environ.get("EMAIL_PASSWORD2")

if email == None or password == None:
    print(f"email:{email}; password:{password}")
    exit(0)


def send_email(body):
    receiver = 'jablonski.norbert@gmail.com'
    try:
        yag = yagmail.SMTP(user=email, password=password)
        yag.send(to=receiver, subject="Alert cenowy", contents='mail.html',attachments='Fig/graph.png')
        print("Mail wysłany")
    except Exception as e:
        print("Problem z wyslaniem meila: {}".format(e))


def prepare_mail(prices):
    body = make_template(prices)
    write_to_file(body)
    return body


def write_to_file(content):
    with open('mail.html', 'w') as f:
        print(content, file=f)


body=prepare_mail(piv.to_html(classes='mystyle'))
send_email(body)
print(piv)
