import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

MY_EMAIL = "adek.konto.testowe@gmail.com"
MY_PASSWORD = "bjtbogzysexemnvk"

ACCEPT_ENCODING = "gzip, deflate"
ACCEPT_LANGUAGE = "pl,en-US;q=0.7,en;q=0.3"
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"

#--------------------- GET ITEM PAGE ---------------------#

item_url = "https://www.amazon.com/NVIDIA-RTX-3090-Founders-Graphics/dp/B08HR6ZBYJ/ref=sr_1_1?crid=WU8PFI66I6J3&keywords=nvidia+geforce+rtx+3090&qid=1661199145&s=computers-intl-ship&sprefix=GeForce%2Ccomputers-intl-ship%2C198&sr=1-1"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
    "Accept-Encoding": ACCEPT_ENCODING
}

response = requests.get(item_url, headers=headers)
item_page = response.text

#--------------------- GET ITEM PRICE ---------------------#

soup = BeautifulSoup(item_page, "lxml")
amazon_item_tag = soup.find(name="span", class_="a-offscreen")
item_price = amazon_item_tag.getText().split('$')[1].replace(',', '')
#float_item_price = float(item_price)
float_item_price = 536.00

amazon_item_name = soup.find(name="span", id="productTitle")
product_name = amazon_item_name.getText()

#--------------------- LET ME KNOW WHEN TO BUY ---------------------#

target_price = float(1300.00)

if float_item_price <= target_price:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="adriandrewniak19@gmail.com",
            msg = f"Subject:Discount time!\n\nYou can finally buy {product_name}\nLink for that product {item_url}\nActual price is: {item_price}."
        )
