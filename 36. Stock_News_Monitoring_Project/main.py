"""goal: to monitor the stock price for the stock that I bought
and know the reason for the change,
then decide to sell, buy more or hold

How it works:
1. Figure out if the stock price that I bought up or down in percentage
2. if the change 5% or more, get 3 news pieces and
3. send myself an SMS with % change and news
4. check the stock price daily"""

import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


STOCK_API_KEY = "75LLZ705TD61ET73"
NEWS_API_KEY = "9323aa9d81ca4a408877cc6ed4413727"
TWILIO_SID = "ACd395ab8f006ee816a1d37ce5d760e140"
TWILIO_AUTH_TOKEN = "353d4bd36f77dd6fecb0f4478f3b4844"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co
# Find out if the STOCK price change by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

# Get closing stock price of yesterday
yesterday_closing_price = float(data_list[0]["4. close"])

# Get closing stock price of the day before yesterday
day_before_yesterday_closing_price = float(data_list[1]["4. close"])

# Find the difference and make it positive
difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
diff_percent = (difference / yesterday_closing_price) * 100

if diff_percent > 5:
    ## STEP 2: Use https://newsapi.org,
    # get top 3 company news pieces from news API
    news_params = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
        "language": "en"
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"][: 3]

    ## STEP 3: Use https://www.twilio.com, send myself an SMS
    # format the message to include percentage change and news title and description
    formatted_articles = [f"{STOCK_NAME}: Headline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    # Send each article as a separate message via Twilio
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+19705338693',
            to='[Twilio Verified Phone Number]'
        )

    print(message.status)


