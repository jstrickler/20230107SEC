from pprint import pprint
import os
import requests
import sqlite3
from edgar_user_agent import EDGAR_USER_AGENT

# headers for GET requests
GET_HEADERS = {
    "User-Agent": EDGAR_USER_AGENT
}

TAXONOMY = 'us-gaap'
CONCEPT = "AccountsPayableCurrent"
YEAR = 2022
QUARTER = 3

# https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json
url = f"https://data.sec.gov/api/xbrl/frames/{TAXONOMY}/{CONCEPT}/USD/CY{YEAR}Q{QUARTER}I.json"

response = requests.get(url, headers=GET_HEADERS)

raw_data = response.json().get('data')


CREATE_TABLE = """
create table edgar_frames (
accn varchar(32) primary key,
cik char(13),
entity varchar(128),
loc varchar(16),
end date,
val integer
)
"""

INSERT_CIK = """
    insert into edgar_frames 
    (accn, cik, entity, loc, end, val) 
    values (?, ?, ?, ?, ?, ?)
"""

DB_NAME = 'edgar_frames.db'
if os.path.exists(DB_NAME):
    os.remove(DB_NAME)

with sqlite3.connect('edgar_frames.db') as eframes:
    eframes.execute(CREATE_TABLE)
    eframes.executemany(INSERT_CIK, [list(r.values()) for r in raw_data])