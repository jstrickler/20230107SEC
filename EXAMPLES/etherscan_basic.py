import requests
from etherscan_api_key import ETHERSCAN_API_KEY

URL = "https://api.etherscan.io/api"
WALLET_ADDRESS = "0x4976a4a02f38326660d17bf34b431dc6e2eb2327" 
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
    