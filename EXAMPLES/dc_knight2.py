from dataclasses import dataclass, field, InitVar

@dataclass
class Knight:
    name: str
    title: str = field(init=False)
    favorite_color: str = field(init=False)
    quest: str = field(init=False)
    comment: str = field(repr=False, init=False)

    def __post_init__(self):
        with open("../DATA/knights.txt") as knights_in:
            for raw_line in knights_in:
                name, title, color, quest, comment = raw_line.rstrip().split(':')
                if name == self.name:
                    self.title = title
                    self.favorite_color = color
                    self.quest = quest
                    self.comment = comment
                    break
            else:
                raise ValueError(f"{self.name} not found")


k = Knight('Arthur')
print(k)

try:
    k = Knight('Mortimer')
except ValueError as err:
    print(err)
else:
    print(k)

