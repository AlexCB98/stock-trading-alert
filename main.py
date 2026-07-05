import requests
import os
from dotenv import load_dotenv

load_dotenv()

STOCK_ENDPOINT = 'NVDA'
NEWS_ENDPOINT = 'https://newsapi.org/v2/everything'
API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')

stock_url = 'https://www.alphavantage.co/query'

stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_ENDPOINT,
    'outputsize': 'compact',
    'apikey': API_KEY,
}

response = requests.get(
    url=stock_url,
    params=stock_parameters,
)
response.raise_for_status()
data = response.json()

stock_name = data['Meta Data']['2. Symbol']
daily_data = data['Time Series (Daily)']

dates = list(daily_data.keys())
latest_date = dates[0]
previous_date = dates[1]

latest_close = float(daily_data[latest_date]['4. close'])
previous_close = float(daily_data[previous_date]['4. close'])


diff = latest_close - previous_close
percentage_diff = round(diff / previous_close * 100, 2)

if abs(percentage_diff) > 5:
    print(f'{STOCK_ENDPOINT} changed by {percentage_diff}')




