from pprint import pprint
import requests
from etherscan_api_key import ETHERSCAN_API_KEY


# /api?module=account&action=getminedblocks&address=0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b&blocktype=blocks&page=1&offset=10&apikey=YourApiKeyToken

URL = "https://api.etherscan.io/api"
WALLET_ADDRESS = "0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b" 

params = {
    'module': 'account',
    'action': 'getminedblocks',
    'address': WALLET_ADDRESS,
    'blocktype': 'blocks',  # can be 'blocks' or 'uncles'
    'page': 1,
    'offset': 10,
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    data = response.json()
    results = data['result']
    pprint(results)
