from dataclasses import dataclass, field
from sec_edgar_api import EdgarClient
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
        edgar = EdgarClient(EDGAR_USER_AGENT)
        data = edgar.get_company_concept(
            cik=self.cik, 
            taxonomy=self.taxonomy, 
            tag=self.tag
        )

        usd_units = data['units']['USD']
        for unit in usd_units:
            fact = CompanyConceptFact(
                accn=unit['accn'],
                end=unit['end'],
                filed=unit['filed'],
                form=unit['form'],
                filing_period=unit['fp'],
                frame=unit.get('frame'),
                fiscal_year=unit['fy'],
                value=unit['val'] // 1000000, # value in millions
            )
            self.facts.append(fact)

if __name__ == "__main__":
    CIK = "320193"  # Apple, Inc.
    TAG = "AccountsPayableCurrent"

    cc = CompanyConcept(cik=CIK, taxonomy='us-gaap', tag=TAG)
    # print(cc)

    print(cc.facts[0])
    print()
    for fact in cc.facts[:10]:
        print(fact.form, fact.fiscal_year, fact.value)
        print('-' * 10)
