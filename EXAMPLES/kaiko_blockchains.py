import requests

base_url = 'https://reference-data-api.kaiko.io/'

url = base_url + 'v1/blockchains'

headers = {'accept': 'application/json'}

response = requests.get(url, headers=headers)

json_data = response.json()

data = json_data.get('data')

for blockchain in data[:10]:
    print(blockchain)
    print("-" * 10)

print("count:", len(data))