from dataclasses import dataclass, astuple
from enum import Enum, auto
from typing import Union, ClassVar
import re

class Direction(Enum):
    NONE: int = auto()
    NORTH: int = auto()
    SOUTH: int = auto()
    EAST: int = auto()
    WEST: int = auto()

@dataclass
class Coordinate:
    angle: float = 0.0
    direction: Direction = Direction.NONE

@dataclass
class Latitude(Coordinate):
    def __post_init__(self):
        if self.direction not in (Direction.NORTH, Direction.SOUTH):
            raise ValueError("Direction for Latitude can only be NORTH or SOUTH")

@dataclass
class Longitude(Coordinate):
    def __post_init__(self):
        if self.direction not in (Direction.EAST, Direction.WEST):
            raise ValueError("Direction for Longitude can only be EAST or WEST")

@dataclass
class GeoPoint:
    RX_COORDINATE_STRING: ClassVar = re.compile(r'(?P<angle>\d+\.\d+)(?P<direction>.*)')

    latitude: Union[Latitude, str]
    longitude: Union[Longitude, str]

    def __post_init__(self):
        if isinstance(self.latitude, str):
            angle, direction = self._parse_coord_str(self.latitude)
            self.latitude = Latitude(angle, direction)

        if isinstance(self.longitude, str):
            angle, direction = self._parse_coord_str(self.longitude)
            self.longitude = Longitude(angle, direction)

    def _parse_coord_str(self, coord_str):
        raw_angle, raw_direction = self.RX_COORDINATE_STRING.search(coord_str).groups()
        if raw_direction == 'N':
            direction = Direction.NORTH
        elif raw_direction == 'S':
            direction = Direction.SOUTH
        elif raw_direction == 'E':
            direction = Direction.EAST
        elif raw_direction == 'W':
            direction = Direction.WEST
        else:
            raise ValueError("Direction must be N, S, E, or W")
        return float(raw_angle), direction

    def __iter__(self):
        yield from astuple(self)

if __name__ == '__main__':

    gp1 = GeoPoint(Latitude(37.4220, Direction.NORTH), Longitude(122.0841, Direction.WEST))

    print(gp1)
    lat, lon = gp1
    print("lat, lon:", lat, lon)

    gp2 = GeoPoint('37.4220N', '122.0841W')
    print(gp2)
    print(gp2.latitude)
    print(gp2.longitude)
    print(type(gp2.longitude.angle))
