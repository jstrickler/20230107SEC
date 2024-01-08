import requests
from etherscan_api_key import ETHERSCAN_API_KEY


# /api?module=transaction&action=getstatus&txhash=0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a&apikey=YourApiKeyToken

URL = "https://api.etherscan.io/api"
TX_HASH = "0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a" 


params = {
    'module': 'transaction',
    'action': 'getstatus',
    'txhash': TX_HASH,
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    data = response.json()
    results = data['result']
    print(results)   # isError:  0 == pass, 1 == fail


