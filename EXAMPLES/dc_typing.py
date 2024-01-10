import sys
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any, Union  # Import needed types from typing
from datetime import date

@dataclass
class PhoneNumber:  # Create dataclass
    number: str  # Class has one member

@dataclass
class AddressBookEntry:
    title: Optional[str]  # The title field can be a str or None
    first_name: str
    middle_name: Optional[str]
    last_name: str
    phone_numbers: list[PhoneNumber]  # phone_numbers is a list of PhoneNumber types
    # note: as of 3.9, list[PhoneNumber] is valid (also dict, tuple, set, frozenset)
    birthday: date

if __name__ == '__main__':

    p = AddressBookEntry("Mr.", "Bob", "J.", "Smith", [PhoneNumber('919-872-9302')],
                         date(1978, 12, 10))
    print(p)
    print(p.last_name)
    print(p.phone_numbers[0])
    p.phone_numbers.append(PhoneNumber('919-239-7204'))  # Type checkers will report an error if anything but a PhoneNumber is appended to phone_numbers
    print(p)

