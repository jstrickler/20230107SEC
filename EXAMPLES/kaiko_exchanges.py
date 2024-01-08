import requests

base_url = 'https://reference-data-api.kaiko.io/'

url = base_url + 'v1/exchanges'

headers = {'accept': 'application/json'}  # not really needed!

response = requests.get(url, headers=headers)

json_data = response.json()

data = json_data.get('data')

for exchange in data[:10]:
    print(exchange)
    print("-" * 10)
print()
count = len(data)
print(f"count: {count}")