import requests
from config import COINGECKO_API_URL

def get_crypto_price(crypto_id='bitcoin'):
    url = f"{COINGECKO_API_URL}/simple/price"
    params = {
        'ids': crypto_id,
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data[crypto_id]['usd']
