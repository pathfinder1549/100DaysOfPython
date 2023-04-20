import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# set root dir, load .env
base_folder = os.path.dirname(__file__)
env_path = os.path.join(base_folder, ".env.txt")
load_dotenv(env_path)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"




## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def stock_moving(stock: str) -> bool:
    # request stock time series from api
    alpha_key = os.getenv("alpha_api_key")      #https://www.alphavantage.co/support/#api-key
    alpha_endpoint = "https://www.alphavantage.co/query"
    alpha_params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock,
        "apikey": alpha_key,
    }
    r = requests.get(url=alpha_endpoint, params=alpha_params)
    stock_time_series = r.json()["Time Series (Daily)"]

    # create date strings for time series keys at one day interval
    td = timedelta(days=1)
    date_today = datetime.now()
    date_start = date_today - 2 * td
    date_end = date_today - td
    date_today_str = f"{date_today.year}-{date_today.month:02}-{date_today.day:02}"
    date_start_str = f"{date_start.year}-{date_start.month:02}-{date_start.day:02}"
    date_end_str = f"{date_end.year}-{date_end.month:02}-{date_end.day:02}"
    
    # find closing price for interval start and end, delta %
    price_start = float(stock_time_series[date_start_str]["4. close"])
    price_end = float(stock_time_series[date_end_str]["4. close"])
    delta_pct = (price_end - price_start) / price_start * 100

    # print values and delta for testing
    print(f"{stock} {date_start_str} closing price: {price_start}")
    print(f"{stock} {date_end_str} closing price: {price_end}")
    print(f"{stock} 24H movement: {delta_pct:.2f}%")

    # flag if delta is over 5%
    if delta_pct >= 5:
        return True
    else:
        return False

if stock_moving(STOCK):
    print("Stock is moving!")
else:
    print("Stock is stable.")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_headlines(stock: str) -> list:
    # request news related to stock from api, limit to 3 top results
    news_key = os.getenv("news_api_key")      #https://newsapi.org/docs/get-started
    news_endpoint = "https://newsapi.org/v2/everything"
    news_params = {
        "q": stock,
        "searchIn": "title",
        "language": "en",
        "apikey": news_key,
    }
    r = requests.get(url=news_endpoint, params=news_params)
    news_articles = r.json()["articles"][:3]

    # return new list with only title, desc, and url
    article_list = []
    for article in news_articles:
        new_article = {
            "Headline": article["title"],
            "Brief": article["description"],
            "Link": article["url"],
        }
        article_list.append(new_article)
    return article_list
    
news_list = get_headlines(STOCK)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

# skipping twilio sms integration, no trial acct
# https://www.twilio.com/try-twilio for api and trial info
# printing sample sms message below

print(f"{STOCK} Trending News:")
for news in news_list:
    print(news["Headline"])

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

