from dataclasses import dataclass, field
from datetime import date
from typing import Union, Iterable

@dataclass()
class ComputerPerson:

    first_name: str
    last_name: str
    organization: str
    birth_date: Union[date, Iterable[int]]  # birth_date can be initialized with date object or any iterable with year, month, day

    full_name: field(init=False) = None # init() does not expect this member variable

    def __post_init__(self):  # postinit() happens after init()
        self.full_name = f'{self.first_name} {self.last_name}'

        if isinstance(self.birth_date, Iterable):  # if birth_date is not already a date, convert it
            self.birth_date = date(*self.birth_date)

if __name__ == '__main__':

    p1 = ComputerPerson(first_name='Bill', last_name='Gates', organization="Microsoft", birth_date=date(1955, 10, 28))  # instantiate ComputerPerson with date object
    print(p1)
    print(p1.full_name, p1.birth_date, p1.birth_date.year)
    print()

    p2 = ComputerPerson('Steve', 'Jobs', 'Apple', (1955,2,24))  # instantiate ComputerPerson with list of ints
    print(p2)
    print(p2.full_name, p2.birth_date, p2.birth_date.year)

