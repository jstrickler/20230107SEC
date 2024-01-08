from dataclasses import dataclass, field
from pprint import pprint

@dataclass
class Knight:
    name: str
    title: str
    favorite_color: str
    quest: str
    comment: str = field(repr=False)


if __name__ == '__main__':

    knights = []
    with open("../DATA/knights.txt") as knights_in:
        knights = [Knight(*line.rstrip().split(':')) for line in knights_in]

    for knight in knights:
        print(knight.title, knight.name)
    print()

    for knight in knights:
        print(knight)
    print()

