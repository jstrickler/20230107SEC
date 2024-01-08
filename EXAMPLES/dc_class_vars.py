from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Person:
    PERSON_COUNT: ClassVar = 0  # declare and initialize class variable (does not become a member variable)
    first_name: str  # member variable
    last_name: str

    def __post_init__(self):
        Person.PERSON_COUNT += 1  # increment class variable on instance creation

    @classmethod
    def get_census(cls):
        return cls.PERSON_COUNT  # access class variable


if __name__ == '__main__':
    p1 = Person('Guido', 'Van Rossum')
    p2 = Person('Larry', 'Wall')
    p3 = Person('Gates', 'Bill')
    print(Person.get_census())  # get_census() can be called from instance or class
