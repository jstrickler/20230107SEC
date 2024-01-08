from zipfile import ZipFile
import os
import sqlite3
import json

import requests
from edgar_user_agent import EDGAR_USER_AGENT

CREATE_TABLE = """
create table cik_lookup (
cik char(13) primary key,
entity varchar(128)
)
"""

INSERT_CIK = """
    insert into cik_lookup (cik, entity) values (?, ?)
"""


COMPANY_FACTS_URL = "https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip"


GET_HEADERS = {
    "User-Agent": EDGAR_USER_AGENT
}

response = requests.get(COMPANY_FACTS_URL, headers=GET_HEADERS)

facts_zip = "edgar_bulk_co_facts.zip"

if not os.path.exists(facts_zip):
    print("Please run 'edgar_bulk_download.py' before running this script")
    exit(1)

with sqlite3.connect('cik_lookup.db') as cikdb:
    cikdb.execute(CREATE_TABLE)  

    with ZipFile(facts_zip) as zip:
        for company_file_name in zip.namelist():
            cik = company_file_name.removesuffix('.json')
            with zip.open(company_file_name) as company_file:
                raw_data = company_file.read()
                data = json.loads(raw_data)
                entity_name = data.get('entityName', 'NONE')
                cikdb.execute(INSERT_CIK, [cik, entity_name])
                print(cik, entity_name)
