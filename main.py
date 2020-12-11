from data import dane
import yagmail
import os
from template import make_template
import datetime
from pandas_operations import piv, df_produkty

now = datetime.date.today()  # data do pliku
dtime = datetime.datetime.now()

email = os.environ.get('EMAIL_USER2')
password = os.environ.get("EMAIL_PASSWORD2")

if email == None or password == None:
    print(f"email:{email}; password:{password}; time: {dtime}")
    exit(0)


def send_email(body):
    receiver = 'jablonski.norbert@gmail.com'
    try:
        yag = yagmail.SMTP(user=email, password=password)
        yag.send(to=receiver, subject="Alert cenowy", contents='mail.html',
                 attachments=['Fig/graph.png',"Dane/all_data.csv"])
        print(f"Mail wysłany - {dtime}")
    except Exception as e:
        print("{} Problem z wyslaniem meila: {}".format(dtime,e))


def write_to_file(content):
    with open('mail.html', 'w') as f:
        print(content, file=f)
    print(f"Mail zapisany - {dtime}")


def prepare_mail(content):
    body = make_template(content)
    write_to_file(body)
    return body


body = prepare_mail([piv.to_html(classes='mystyle'), df_produkty.to_html(classes="mystyle")])
send_email(body)
print(piv)
