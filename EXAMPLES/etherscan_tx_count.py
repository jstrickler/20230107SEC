import requests
from etherscan_api_key import ETHERSCAN_API_KEY

# /api?module=proxy&action=eth_getTransactionCount&address=0x2910543af39aba0cd09dbb2d50200b3e800a63d2&tag=latest&apikey=YourApiKeyToken

URL = "https://api.etherscan.io/api"
WALLET_ADDRESS = "0x2910543af39aba0cd09dbb2d50200b3e800a63d2" 
TAG = "latest"

params = {
    'module': 'proxy',
    'action': 'eth_getTransactionCount',
    'address': WALLET_ADDRESS,
    'tag': TAG,
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    data = response.json()
    results = data['result']
    print(results, int(results, 16))  # hex string and decimal number
