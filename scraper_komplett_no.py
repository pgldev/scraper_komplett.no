import requests


from bs4 import BeautifulSoup

import smtplib


#Current settings. This works for komplett.no but is easily changeable to another website. This is made to notify you when a price on an item you want drops bellow a certen ammount. (set in wanted_price = )

URL = "https://www.komplett.no/product/1129544/mobiler-klokker/mobiltelefoner/oneplus-7-pro-8gb256gb-almond"

# User agent. You can google this for another one

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"}



# Fill here with your email information!


#Senders email

sender_email = "test@gmai1.c0m"

#Recipient email

recipient_email = "test@gmai1.c0m"

#Smtp mail server adress (smtp.gmail.com) for gmail

smtp_mail_server = "smtp.gmail.com"

# Mailserver port (587) for gmail

smtp_mail_server_port = 587

smtp_mail_server_username = "test@gmai1.c0m"

smtp_mail_server_apppassword = "APPPASSWORD"

# The price you want to get informed when it goes bellow.

wanted_price = 6000


page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

#gets the title of the item. tested with komplett.no items

title = soup.find("h1").get_text()

#Finds the price on the item on komplett.no

price = soup.find("div", "product-price").get_text()

#this under cleans up the price and then convert it to a float

price_convert = price.replace(",-", "")

price_convert01 = price_convert.replace("\xa0", "")

price_convert02 = float(price_convert01)


print(title,price_convert02,wanted_price)




def price_check():

    if wanted_price <= price_convert02:

        send_mail()

    else:

        send_mail_2()


def send_mail():

    server = smtplib.SMTP(smtp_mail_server, smtp_mail_server_port)

    server.ehlo()

    server.starttls()

    server.ehlo()

    server.login(smtp_mail_server_username, smtp_mail_server_apppassword)

    subject = ("Price is to high!", price_convert02)

    body = (URL, "Check this link!", title)

    msg = f"Subject: {subject}\n\n\n{body}"

    server.sendmail(

        sender_email,

        recipient_email,

        msg

    )

    print("Mail sendt, price to high!")

    server.quit()


def send_mail_2():

    server = smtplib.SMTP(smtp_mail_server, smtp_mail_server_port)

    server.ehlo()

    server.starttls()

    server.ehlo()

    server.login(smtp_mail_server_username, smtp_mail_server_apppassword)

    subject = "Price is bellow wanted!", price_convert02

    body = (URL, "Check this link!", title)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(

        sender_email,

        recipient_email,

        msg

    )

    print("Mail sendt, price is bellow!")

    server.quit()


price_check()
