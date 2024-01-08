from dataclasses import dataclass
from datetime import date

@dataclass()
class ComputerPerson():

    first_name: str
    last_name: str
    product: str
    dob: int

if __name__ == '__main__':
    p1 = ComputerPerson(first_name='Bill', last_name='Gates', product="Microsoft", dob=date(1955, 10, 28))


    print(type(p1))
    print(p1)

    print(repr(p1))

    print(p1.first_name, p1.dob)
    print()

    p1.first_name = 'Henry'

    print(p1)
    print()

    p2 = ComputerPerson('Linus', 'Torvalds', 'Linux', date(1969, 12, 28))
    print(p2)
