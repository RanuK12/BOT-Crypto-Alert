import requests
from config import COINGECKO_API_URL

def get_crypto_price(crypto_id):
    response = requests.get(f'{COINGECKO_API_URL}/simple/price', params={
        'ids': crypto_id,
        'vs_currencies': 'usd'
    })
    data = response.json()
    return data[crypto_id]['usd']

if __name__ == "__main__":
    print(get_crypto_price('bitcoin'))
