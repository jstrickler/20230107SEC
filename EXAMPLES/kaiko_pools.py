import requests

base_url = 'https://reference-data-api.kaiko.io/'

url = base_url + 'v1/pools'

headers = {'accept': 'application/json', 'x-api-key': 'SEC-API-KEY'}

response = requests.get(url, headers=headers)

json_data = response.json()

data = json_data.get('data')

for pool in data[:3]:
    print(pool)
    print("-" * 10)

print("count:", len(data))