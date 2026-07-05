import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

STOCK_SYMBOL = 'NVDA'
COMPANY_NAME = 'NVIDIA'

STOCK_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

MY_EMAIL = os.environ.get('MY_EMAIL')
MY_PASSWORD = os.environ.get('MY_EMAIL_PASSWORD')


def get_stock_data():
    stock_url = 'https://www.alphavantage.co/query'

    stock_parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK_SYMBOL,
        'outputsize': 'compact',
        'apikey': STOCK_API_KEY,
    }

    stock_response = requests.get(
        url=stock_url,
        params=stock_parameters,
    )
    stock_response.raise_for_status()

    return stock_response.json()


def get_news_data():
    news_url = 'https://newsapi.org/v2/everything'

    news_parameters = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
        'language': 'en',
        'sortBy': 'publishedAt',
    }

    news_response = requests.get(
        url=news_url,
        params=news_parameters,
    )
    news_response.raise_for_status()

    return news_response.json()


stock_data = get_stock_data()

stock_name = stock_data['Meta Data']['2. Symbol']
daily_data = stock_data['Time Series (Daily)']

dates = list(daily_data.keys())
latest_date = dates[0]
previous_date = dates[1]

latest_close = float(daily_data[latest_date]['4. close'])
previous_close = float(daily_data[previous_date]['4. close'])

diff = latest_close - previous_close
percentage_diff = round(diff / previous_close * 100, 2)

if percentage_diff > 0:
    direction = 'UP'
else:
    direction = 'DOWN'

if abs(percentage_diff) > 1:
    news_data = get_news_data()

    articles = news_data['articles']
    three_articles = articles[:3]

    formatted_articles = [
        f'Headline: {article["title"]}\n'
        f'Brief: {article["description"]}'
        for article in three_articles
    ]

    email_body = '\n\n'.join(formatted_articles)

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=(
                f'Subject: {COMPANY_NAME} {direction} {abs(percentage_diff)}%\n\n'
                f'{STOCK_SYMBOL} changed by {percentage_diff}%.\n\n'
                f'{email_body}'
            )
        )