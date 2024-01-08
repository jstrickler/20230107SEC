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

TAXONOMY = 'us-gaap'
CONCEPT = "AccountsPayableCurrent"

# e.g., https://data.sec.gov/api/xbrl/companyconcept/
#                 CIK##########/us-gaap/AccountsPayableCurrent.json
url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{CIK}/{TAXONOMY}/{CONCEPT}.json"

response = requests.get(url, headers=GET_HEADERS)
if response.status_code == requests.codes.OK:
    content_type = response.headers.get('content-type', "")
    if 'json' in content_type.lower():
        data = response.json()
    else:
        raise Exception("Request returned %s, not JSON", content_type)
else: 
    raise Exception("Request failed with HTTP code %d", response.status_code)

pprint(data)