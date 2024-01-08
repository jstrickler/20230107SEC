import time
import requests
from edgar_user_agent import EDGAR_USER_AGENT

CIK = "0000320193"  # Apple, Inc.

URL = f"https://data.sec.gov/submissions/CIK{CIK}.json"

with requests.session() as session:
    session.headers['user-agent'] = EDGAR_USER_AGENT
    response = session.get(URL)
    if response.status_code == requests.codes.OK:
        submission_data = response.json()
        metadata_keys = ", ".join(submission_data.keys())
        print(metadata_keys)
        print()
        recent_filings = submission_data['filings']['recent']
#        print(recent_filings)
        print()
        files = submission_data['filings']['files']  # if any separate files
        print(files)

        file_name = files[0]['name']
        
        URL = f"https://data.sec.gov/submissions/{file_name}"
        
        response = session.get(URL)
#        print(response.json())
