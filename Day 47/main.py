import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.

MY_EMAIL = os.getenv("MY_EMAIL")
TO_EMAIL = os.getenv("TO_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")
URL = "https://www.amazon.in/CuberSpeed-Qifan-Stickerless-Bright-MoFangGe/dp/B07R9YR3Y7/ref=sr_1_15?crid=2GFHN5ZKWWD0Y&keywords=6x6+rubik%27s+cube&qid=1671716968&sprefix=6x6%2Caps%2C224&sr=8-15"
header = {
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8,mr;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}


def send_email(title, price, link):
    email_message = f"Subject: Amazon Price Alert\n\nProduct name: {title}\nCurrent Price: {price}\nBuy Here: {link}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=email_message)


response = requests.get(URL, headers=header)
webpage = response.text
soup = BeautifulSoup(webpage, "lxml")

price_tag = soup.find(name="span", class_="a-price-whole")

price = ""
for num in price_tag.getText().split(","):
    price = price + num

title = soup.find(name="span", id="productTitle").getText()
price = float(price)
link = URL

if price < 1350:
    send_email(title, price, link)

print("Successful")
