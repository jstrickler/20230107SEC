from datetime import datetime
import requests

base_url = 'https://reference-data-api.kaiko.io/'

url = base_url + 'v1/instruments'

headers = {'accept': 'application/json'}
params = {'exchange_code': 'bnce'}

response = requests.get(url, headers=headers, params=params)

json_data = response.json()

data = json_data.get('data')

for instrument in data[-10:]:
    raw_ts = instrument['trade_start_timestamp']
    # KaiKo timestamp is milliseconds since 1/1/1970
    ts = datetime.fromtimestamp(raw_ts / 1000)
    print(instrument['code'], ts.strftime("%x %X"))
    print("-" * 10)

print("count:", len(data))