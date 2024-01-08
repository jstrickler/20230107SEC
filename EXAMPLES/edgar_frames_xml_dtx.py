import csv
import requests
from dicttoxml import dicttoxml
from edgar_user_agent import EDGAR_USER_AGENT

# headers for GET requests
GET_HEADERS = {
    "User-Agent": EDGAR_USER_AGENT
}

TAXONOMY = 'us-gaap'
CONCEPT = "AccountsPayableCurrent"
YEAR = 2019
QUARTER = 2

url = f"https://data.sec.gov/api/xbrl/frames/{TAXONOMY}/{CONCEPT}/USD/CY{YEAR}Q{QUARTER}I.json"
print(url)

response = requests.get(url, headers=GET_HEADERS)
if response.status_code == requests.codes.OK:
    content_type = response.headers.get('content-type', "")
    if 'json' in content_type.lower():
        facts_data = response.json()
    else:
        raise Exception("Request returned %s, not JSON", content_type)
else: 
    raise Exception("Request failed with HTTP code %d", response.status_code)

frames = facts_data.get('data')

def make_item_name(parent):
    return parent.removesuffix('s')

if frames:
    xml_doc = dicttoxml(
        frames,
        custom_root='frames',
        attr_type=False,
        include_encoding=False,
        item_func=make_item_name,
    )
    with open('edgar_frames.xml', 'wb') as frames_out:
        frames_out.write(xml_doc)
    