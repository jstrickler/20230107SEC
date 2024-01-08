from pprint import pprint
import requests
from etherscan_api_key import ETHERSCAN_API_KEY

# https://api.etherscan.io/api?module=stats&action=ethprice&apikey=YourApiKeyToken

URL = "https://api.etherscan.io/api"

params = {
    'module': 'stats',
    'action': 'ethprice',
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    data = response.json()
    results = data['result']
    pprint(results)
