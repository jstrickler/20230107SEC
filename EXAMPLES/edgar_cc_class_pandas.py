from dataclasses import dataclass, field
#from sec_edgar_api import EdgarClient
import pandas as pd
import requests
from edgar_user_agent import EDGAR_USER_AGENT

@dataclass
class CompanyConceptFact:
    accn: str
    end: str
    filed: str
    form: str
    filing_period: str
    frame: str
    fiscal_year: int
    value: int

@dataclass
class CompanyConcept:
    cik: str
    taxonomy: str
    tag: str
    facts: list[CompanyConceptFact] = field(init=False, default_factory=list)
    
    def __post_init__(self):
        data = self._get_company_concept()
        usd_units = data['units']['USD']
        for unit in usd_units:
            fact = CompanyConceptFact(
                accn=unit['accn'],
                end=unit['end'],
                filed=unit['filed'],
                form=unit['form'],
                filing_period=unit['fp'],
                frame=unit.get('frame'), # not always present
                fiscal_year=unit['fy'],
                value=unit['val'] // 1000000, # value in millions
            )
            self.facts.append(fact)

    def _get_company_concept(self):
        # edgar = EdgarClient(EDGAR_USER_AGENT)
        # edgar._session.verify = False  # may be needed...
        # data = edgar.get_company_concept(
        #     cik=self.cik, 
        #     taxonomy=self.taxonomy, 
        #     tag=self.tag
        # )
        url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{int(self.cik):010d}/{self.taxonomy}/{self.tag}.json"
        response = requests.get(
            url,
            headers={
                'user-agent':EDGAR_USER_AGENT,
            }
        )
        return response.json()



if __name__ == "__main__":
    CIKS = [
        "320193",  # Apple
        "789019", # Microsoft
        "320187", # Nike
    ]
    TAXONOMY = 'us-gaap'
    TAG = "AccountsPayableCurrent"

    dataframes = []
    for cik in CIKS:
        cc = CompanyConcept(cik=cik, taxonomy=TAXONOMY, tag=TAG)
        df = pd.DataFrame.from_dict(cc.facts)
        df['cik'] = [cik] * len(cc.facts)
        dataframes.append(df)
    
    bigdf = pd.concat(dataframes, ignore_index=True)

    print(bigdf.head())
    print('-' * 60)
    print(bigdf.tail())
    print()
    print(bigdf.iloc[0])
