import requests
from edgar_user_agent import EDGAR_USER_AGENT

COMPANY_FACTS_URL = "https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip"

SUBMISSION_URL = "https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip"

GET_HEADERS = {
    "User-Agent": EDGAR_USER_AGENT
}

response = requests.get(COMPANY_FACTS_URL, headers=GET_HEADERS)

with open("edgar_bulk_co_facts.zip", "wb") as edgar_in:
    edgar_in.write(response.content)

response = requests.get(SUBMISSION_URL, headers=GET_HEADERS)

with open("edgar_bulk_submissions.zip", "wb") as edgar_in:
    edgar_in.write(response.content)
