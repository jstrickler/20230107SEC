import json
from pprint import pprint
import pandas as pd

JSON_DATA_FILE = "brian_sample.json"

with open(JSON_DATA_FILE) as sample_in:
    raw_data = json.load(sample_in)

pprint(raw_data)
print('-' * 60)

df = pd.read_json(JSON_DATA_FILE, orient)
print(df.head())