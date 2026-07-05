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

