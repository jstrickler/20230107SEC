from dataclasses import dataclass

@dataclass
class Point:
    x: int = 0.0  # provide default value for x
    y: int = 0.0

p1 = Point()  # with no arguments to class, uses default value
p2 = Point(3.4, 5.8)  # passing arguments overrides defaults

print(p1, p2)
