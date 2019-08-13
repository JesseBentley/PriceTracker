import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = https://www.amazon.com/Canon-T7-18-55mm-3-5-5-6-Accessory/dp/B07P15K8Q7/ref=sr_1_1?keywords=cannon&qid=1565656955&s=gateway&sr=8-1

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    if(converted_price < 400):
        send_mail()

    title.strip()

def send_mail():
    server = smptlib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email@mail.com', 'password')

    subject = 'Price is in the sweet spot!'
    body = 'https://www.amazon.com/Canon-T7-18-55mm-3-5-5-6-Accessory/dp/B07P15K8Q7/ref=sr_1_1?keywords=cannon&qid=1565656955&s=gateway&sr=8-1 camera is on the low price. Lets do it!'
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'email@mail.com',
        'email@mail.com',
        msg
    )

    print('Mail has been sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60 * 12)