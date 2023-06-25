import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
account_sid = 'AC62e7000b920136b322b59a628669e1d6'

def get_news():
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_parameters = {
        'q': COMPANY_NAME,
        'apiKey': NEWS_API_KEY,
        'pageSize': 3,
        'language': "en",
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    for index in range(3):
        with open(f"{STOCK}.txt", mode='a') as stock_message:
            stock_message.write(f"Headline: {news_data['articles'][index]['title']}\n")
            stock_message.write(f"Brief: {news_data['articles'][index]['description']}\n\n")

def send_sms():
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    with open(f"{STOCK}.txt", mode='r') as stock_message:
        message_content = stock_message.read()
    print(message_content)
    client = Client(account_sid, AUTH_TOKEN)
    message = client.messages.create(
        from_='xxxx',
        to='xxxx',
        body=message_content,
    )
    print(message.status)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={ALPHA_API_KEY}")
response.raise_for_status()
stock_data = response.json()
# print(stock_data)
stock_data_value = list(stock_data['Time Series (Daily)'].values())[:2]
close_price_yesterday = float(stock_data_value[0]['4. close'])
close_price_before_yesterday = float(stock_data_value[1]['4. close'])
# print(f"close rate Yesterday: {close_price_yesterday}")
# print(f"close rate Before Yesterday: {close_price_before_yesterday}")

# Use abs() to get the absolute value
diff_price = close_price_yesterday - close_price_before_yesterday
if diff_price < 0:
    up_down = "Decrease"  #"🔻"
else:
    up_down = "Increase"  #"🔺"
diff_percentage = (abs(diff_price)/close_price_yesterday) * 100
# print(diff_percentage)
if diff_percentage > 3:
    with open(f"{STOCK}.txt", mode='w') as stock_message:
        stock_message.write(f"{STOCK} {up_down} 3%.\n\n")
    get_news()
    send_sms()

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

