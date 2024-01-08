import requests

base_url = 'https://reference-data-api.kaiko.io/'

url = base_url + 'v1/assets'

headers = {'accept': 'application/json'}

response = requests.get(url, headers=headers)

json_data = response.json()

data = json_data.get('data')

for asset in data[:10]:
    print(asset)
    print("-" * 10)

print("count:", len(data))