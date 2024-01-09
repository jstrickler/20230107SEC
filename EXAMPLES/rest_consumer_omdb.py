import requests
from pprint import pprint

with open('omdbapikey.txt') as api_in:
    OMDB_API_KEY = api_in.read().rstrip()

OMDB_URL = "http://www.omdbapi.com"

def main():
    requests_params = {'t': 'Oppenheimer', "apikey": OMDB_API_KEY}
#    proxies = {'https': 'https://www.sec.gov/myproxywhatever'}
    response = requests.get(OMDB_URL, params=requests_params) # , proxies=proxies)
    if response.status_code == requests.codes.OK:
        raw_data = response.json()

        print(f"raw_data['Title']: {raw_data['Title']}")
        print(f"raw_data['Director']: {raw_data['Director']}")
        print(f"raw_data['Year']: {raw_data['Year']}")
        print(f"raw_data['Runtime']: {raw_data['Runtime']}")
        for rating in raw_data.get('Ratings'):
            print("    ", rating['Source'], rating['Value'])

        print()

        print('-' * 60)

        print("raw DATA:")
        pprint(response.json())
        print("really raw data:")
        print(response.content)
    else:
        print(f"response.status_code: {response.status_code}")

if __name__ == '__main__':
    main()
