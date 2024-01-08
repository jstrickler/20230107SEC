from dataclasses import dataclass

@dataclass
class PublishedDateIncomparable():  # Create default dataclass. Only init(), repr(), and eq() are generated.
    year: int
    month: int
    day: int

p1 = PublishedDateIncomparable(2020, 10, 31)  # Create instance of class
p2 = PublishedDateIncomparable(2020, 9, 22)

print("Incomparable:", end=' ')
try:
    result = p1 > p2  # Comparison fails
except TypeError as err:
    print(err)
else:
    print(result)

@dataclass(order=True)  # Create dataclass with order set to True. Comparison methods are generated
class PublishedDateComparable:
    year: int
    month: int
    day: int

p1 = PublishedDateComparable(2020, 10, 31)
p2 = PublishedDateComparable(2020, 9, 22)

print("Comparable:", end=' ')
try:
    result = p1 > p2  # Comparison succeeds
except TypeError as err:
    print(err)
else:
    print(result)
