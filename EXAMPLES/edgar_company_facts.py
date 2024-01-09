import sys
import requests
from pprint import pprint
from edgar_user_agent import EDGAR_USER_AGENT


# headers for GET requests
GET_HEADERS = {
    "User-Agent": EDGAR_USER_AGENT
}

# CIK = "0000320193"  # Apple, Inc.
CIK = "0001467858"  # General Motors
UNIT = "USD"

# https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{CIK}.json"

response = requests.get(url, headers=GET_HEADERS)
if response.status_code == requests.codes.OK:
    content_type = response.headers.get('content-type', "")
    if 'json' in content_type.lower():
        raw_json = response.json()
    else:
        raise Exception("Request returned %s, not JSON", content_type)
else: 
    raise Exception("Request failed with HTTP code %d", response.status_code)

for concept, concept_data in raw_json['facts']['us-gaap'].items(): #  loop over concepts
    print(concept)
    for unit, fact_data in concept_data['units'].items():
        for fact in fact_data:
            if fact['form'] != '10-K':
                continue
            print(fact)
    print()