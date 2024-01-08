from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Foob:
    a: str
    b: str
    c: str = field(init=False, repr=False)

if __name__ == '__main__':
    f = Foob('one', 'two')

print(f)

