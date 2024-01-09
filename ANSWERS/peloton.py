import requests

# headers for GET requests
GET_HEADERS = {
    "User-Agent": "jstrickler@gmail.com"
}

CIK = "0001639825" #  PELOTON INTERACTIVE, INC.
CONCEPT = "EarningsPerShareBasic"

url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{CIK}/us-gaap/{CONCEPT}.json"

response = requests.get(url, headers=GET_HEADERS)
if response.status_code == requests.codes.OK:
    content_type = response.headers.get('content-type', "")
    if 'json' in content_type.lower():
        data = response.json()
    else:
        raise Exception("Request returned %s, not JSON", content_type)
else: 
    raise Exception("Request failed with HTTP code %d", response.status_code)

for fact in data['units']['USD/shares']:
    print(f"{fact['start']} {fact['end']} {fact['val']:8.2f}")