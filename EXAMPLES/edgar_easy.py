from pprint import pprint
from sec_edgar_api import EdgarClient
from edgar_user_agent import EDGAR_USER_AGENT

edgar = EdgarClient(user_agent=EDGAR_USER_AGENT)

CIK = "320193"  # Apple, Inc.

submission_data = edgar.get_submissions(cik=CIK)

recent_filings = submission_data["filings"]["recent"]
for key, value in recent_filings.items():
    print(key, value[:3])  # print  first 3 items for each filing key
print('-' * 60)

ap_current = edgar.get_company_concept(cik=CIK, taxonomy="us-gaap", tag="AccountsPayableCurrent")

usd_units = ap_current['units']['USD']
for i, unit in enumerate(usd_units, 1):
    print(i, unit['filed'], unit['val'])
    if i == 5:
        break
