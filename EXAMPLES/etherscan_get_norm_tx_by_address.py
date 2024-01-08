import requests
from etherscan_api_key import ETHERSCAN_API_KEY


# /api?module=account&action=txlist&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&startblock=0&endblock=99999999&page=1&offset=10&sort=asc&apikey=YourApiKeyToken


URL = "https://api.etherscan.io/api"
WALLET_ADDRESS = "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a"
TAG = "latest"

params = {
    'module': 'account',
    'action': 'txlist',
    'address': WALLET_ADDRESS,
    'startblock': 0,
    'endblock': 99999999,
    'page': 1,
    'offset': 20,
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    data = response.json()
    print(data)
    # data['result'] is list of tx
