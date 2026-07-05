import requests
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_SYMBOL = 'NVDA'
COMPANY_NAME = 'NVIDIA'

STOCK_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

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
    data = stock_response.json()

    return data

def get_news_data():
    news_url = 'https://newsapi.org/v2/everything'

    news_parameters = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME,
    }

    news_response = requests.get(
        url=news_url,
        params=news_parameters,
    )
    news_response.raise_for_status()
    data = news_response.json()

    return data

news_data = get_news_data()
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

articles = news_data['articles']

if abs(percentage_diff) > 1:
    print(articles)




