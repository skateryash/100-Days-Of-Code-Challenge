import os
import requests
from twilio.rest import Client


STOCK = "RELIANCE"
STOCK_SYMBOL = "RELIANCE.BSE"
COMPANY_NAME = "RELIANCE INDS"

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_SYMBOL,
    "apikey": STOCK_API_KEY
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()
yesterday_price = float(stock_data["Time Series (Daily)"]["2022-09-16"]["4. close"])
day_before_yesterday_price = float(stock_data["Time Series (Daily)"]["2022-09-15"]["4. close"])
price_difference = yesterday_price - day_before_yesterday_price
price_difference_percentage = (price_difference / day_before_yesterday_price) * 100

if price_difference_percentage < 0:
    difference = "🔻" + str(round(price_difference_percentage, 2))
else:
    difference = "🔺" + str(round(price_difference_percentage, 2))

if price_difference_percentage > 1:
    news_parameters = {
        "q": STOCK,
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()
    news = news_data["articles"][:3]
    news_heading = [article["title"] for article in news]
    news_description = [article["description"] for article in news]

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    for item in range(0, 3):
        message_body = f"{STOCK}: {difference}\nHeadline: {news_heading[item]}\nBrief: {news_description[item]}"
        message = client.messages \
                .create(
                body=message_body,
                from_=TWILIO_NUMBER,
                to=MY_NUMBER
                )
