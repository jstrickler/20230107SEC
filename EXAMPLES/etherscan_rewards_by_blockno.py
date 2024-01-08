from pprint import pprint
import requests
from etherscan_api_key import ETHERSCAN_API_KEY


# /api?module=block&action=getblockreward&blockno=2165403&apikey=YourApiKeyToken

BLOCK_NUMBER = 2165403

URL = "https://api.etherscan.io/api"

params = {
    'module': 'block',
    'action': 'getblockreward',
    'blockno': BLOCK_NUMBER,
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    data = response.json()
    results = data['result']
    pprint(results)
