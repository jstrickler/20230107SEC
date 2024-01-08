from pprint import pprint
import json

import requests
from etherscan_api_key import ETHERSCAN_API_KEY

# /api?module=contract&action=getabi&address=0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413&apikey=YourApiKeyToken

URL = "https://api.etherscan.io/api"
WALLET_ADDRESS = "0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413" 

params = {
    'module': 'contract',
    'action': 'getabi',
    'address': WALLET_ADDRESS,
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    data = response.json()
    results_json = data['result']
    results = json.loads(results_json)
    pprint(results)
