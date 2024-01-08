"""
dataclass_from_fields
=====================

Illustrate how to create a dataclass from field names, rather than by decorating a class.
"""
from dataclasses import make_dataclass, field

Point = make_dataclass('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1, p2)
print()

class_name = "Person" #: name to use for class

fields = [
    ('first_name', str),
    ('last_name', str),
    ('state', str, field(repr=False))
]

Person = make_dataclass(class_name, fields)  #: create dataclass

if __name__ == '__main__':

    print(Person)

    p = Person("Guido", "Van Rossum", "OR")

    print(p)
