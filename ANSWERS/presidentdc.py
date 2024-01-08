from dataclasses import dataclass
from datetime import date
from typing import Union

def make_date(date_string):
    if date_string == 'NONE':
        return None
    year, month, day = date_string.split('-')
    return date(int(year), int(month), int(day))

@dataclass
class President:
    term: int
    first_name: str
    last_name: str
    birth_date: date
    death_date: Union[date, None]
    birthplace: str
    birth_state: str
    date_took_office: date
    date_left_office: Union[date, None]
    party: str

presidents = []
with open('../DATA/presidents.txt') as presidents_in:
    for raw_line in presidents_in:
        line = raw_line.rstrip()
        (term, last_name, first_name, dob, dod, birthplace,
         birth_state, term_start, term_end, party) = line.split(':')
        p = President(int(term), first_name, last_name, make_date(dob),
            make_date(dod), birthplace,
         birth_state, make_date(term_start), make_date(term_end), party)

        # alternate approach:
        # fields = line.split(':')
        # p = President(*fields)
        # or even
        # p = President(*raw_line.rstrip().split(':'))

        presidents.append(p)

for p in presidents:
    print(f"{p.term:2d} {p.first_name:25.25s} {p.last_name:10s} {p.birth_state:15s} {p.birth_date} {p.party}")

