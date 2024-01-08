import requests

base_url = 'https://reference-data-api.kaiko.io/'

url = base_url + 'v1/instruments'

headers = {'accept': 'application/json'}
params = {'code': '007btc'}

response = requests.get(url, headers=headers, params=params)

json_data = response.json()

data = json_data.get('data')

for instrument in data[:10]:
    print(instrument)
    print("-" * 10)

print("count:", len(data))