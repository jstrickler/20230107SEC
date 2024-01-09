from argparse import ArgumentParser
import os
import requests
from pprint import pprint

parser = ArgumentParser(description="Movie Fetcher")
parser.add_argument("--config_folder", dest="config", help="Folder containing config file")


OMDB_URL = "http://www.omdbapi.com"

MOVIE_TITLES = [
    'Black Panther',
    'Freeze',
    'Top',
    'gun',
    'Bullet Train',
    'Nile',
    'Casablanca',
]

def main():
    args = parser.parse_args()
    if args.config:
        config_path = args.config
    else:
        config_path = "."

    config_file_path = os.path.join(config_path, "omdbapikey.txt")
    with open(config_file_path) as api_in:
        OMDB_API_KEY = api_in.read().rstrip()


    with requests.Session() as session:
        session.params.update({"apikey": OMDB_API_KEY})
        for movie_title in MOVIE_TITLES:
            params = {'t': movie_title}
            response = session.get(OMDB_URL, params=params)
            if response.status_code == requests.codes.OK:
                raw_data = response.json()
                print(f"raw_data['Title']: {raw_data['Title']}")
                print(f"raw_data['Director']: {raw_data['Director']}")
                print(f"raw_data['Year']: {raw_data['Year']}")
                print(f"raw_data['Runtime']: {raw_data['Runtime']}")
                print()



if __name__ == '__main__':
    main()
