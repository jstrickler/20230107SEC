from collections import namedtuple
from dataclasses import make_dataclass, asdict, fields


field_names = ['x', 'y']   # field names
field_types = [int, int]   # field types (only used for dataclass)

PointNT = namedtuple('PointNT', field_names)  # make a named tuple

pnt1 = PointNT(5, 10)  # instantiate named tuple
print(pnt1, pnt1.x, pnt1.y)  # access fields

# dataclass
PointDC = make_dataclass('PointDC', zip(field_names, field_types), order=True)  # make a dataclass, specifying field names and types

pdc1 = PointDC(5, 10)  # instantiate named tuple
print(pdc1, pdc1.x, pdc1.y)  # access fields

print()

pnt2 = PointNT(10, 20)  # make another instance of each type

pdc2 = PointDC(10, 20)

print(pnt2 > pnt1)  # comparison OK (needs `order=True` for dataclass)
print(pdc2 > pdc1)

print(pnt1._asdict())  # export as dict
print(asdict(pdc2))

print(pnt1._fields)  # get field names
print("----")
for f in fields(pdc1):
    print(f)

print()

for p in pnt1, pdc1:  # replace value (OK for dataclass; fails for namedtuple)
    try:
        p.x = 100
    except AttributeError as err:
        print(err)
    else:
        print(p)
