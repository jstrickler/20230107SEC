import requests
from etherscan_api_key import ETHERSCAN_API_KEY

URL = "https://api.etherscan.io/api"
WALLET_ADDRESS = "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a" 
TAG = "latest"

params = {
    'module': 'account',
    'action': 'balance',
    'address': WALLET_ADDRESS,
    'tag': TAG,
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    print(response.json())
