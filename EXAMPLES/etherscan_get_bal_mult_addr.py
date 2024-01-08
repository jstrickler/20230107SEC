import requests
from etherscan_api_key import ETHERSCAN_API_KEY

# Get Ether Balance for multiple Addresses in a single call
# /api?module=account&action=balancemulti&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67&tag=latest&apikey=YourApiKeyToken

URL = "https://api.etherscan.io/api"
WALLET_ADDRESSES = "0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67"  
TAG = "latest"

params = {
    'module': 'account',
    'action': 'balancemulti',
    'address': WALLET_ADDRESSES,
    'tag': TAG,
    'apikey': ETHERSCAN_API_KEY,
}

response = requests.get(URL, params=params)
if response.status_code == requests.codes.OK:
    data = response.json()
    print(data)
    print('-' * 60)
    print(data.get('result'))