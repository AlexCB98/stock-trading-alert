import requests
import os
from dotenv import load_dotenv

load_dotenv()

STOCK = 'NVDA'
API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
URL = 'https://www.alphavantage.co/query'

parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': API_KEY,
}

response = requests.get(
    url=URL,
    params=parameters,
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



