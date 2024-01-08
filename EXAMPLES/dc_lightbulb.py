from dataclasses import dataclass
from enum import Enum, auto

class State(Enum):
    ON = True
    OFF = False


class BulbType(Enum):
    INCANDESCENT = auto()
    FLUORESCENT = auto()
    LED = auto()
    MERCURY_VAPOR = auto()

@dataclass
class LightBulb():
    watts: int
    bulb_type: BulbType = BulbType.INCANDESCENT
    state: State = State.OFF

    def switch(self):
        # self.state = not self.state
        if self.state == State.ON:
            self.state = State.OFF
        else:
            self.state = State.ON

if __name__ == '__main__':

    b1 = LightBulb(100)
    print(b1)

    b1.switch()
    print(b1)

    b1.switch()
    print(b1)

    b1.watts = 75
    print(b1)

    b2 = LightBulb(42, BulbType.LED, State.ON)
    print(b2)

    b3 = LightBulb(bulb_type=BulbType.MERCURY_VAPOR, watts=200, state=State.OFF)
    print(b3)

