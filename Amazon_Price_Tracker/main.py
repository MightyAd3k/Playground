import requests
from bs4 import BeautifulSoup
import lxml


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
#print(amazon_item_tag.getText())
item_price = float(amazon_item_tag.getText())