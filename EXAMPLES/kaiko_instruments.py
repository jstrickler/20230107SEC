import requests

base_url = 'https://reference-data-api.kaiko.io/'

url = base_url + 'v1/instruments'

headers = {'accept': 'application/json'}

response = requests.get(url, headers=headers)

json_data = response.json()

data = json_data.get('data')

for instrument in data[:3]:
    print(instrument)
    print("-" * 10)

print("count:", len(data))