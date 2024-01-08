from collections import namedtuple

person = ['Joe', 'Schmoe', 'Schenectady', 'NY']  # Create list with data. No field names
print("list:", person[0], person[1], "repr:", repr(person))

person = 'Joe', 'Schmoe', 'Schenectady', 'NY'  # Create tuple with data. No field names, and read-only
print("tuple:", person[0], person[1], "repr:", repr(person))

person = {'first_name': 'Joe', 'last_name': 'Schmoe', 'city': 'Schenectady', 'state': 'NY'}  # Create dict with data. Field names, read-write, but field names (keys) are not fixed
print("dict:", person['first_name'], person['last_name'], "repr:", repr(person))

Person = namedtuple('Person', 'first_name last_name city state')  # Define named tuple
person = Person('Joe', 'Schmoe', 'Schenectady', 'NY')  # Create named tuple with data. Field names, efficient, but read-only
print("named tuple:", person.first_name, person.last_name, "repr:", repr(person))

class Person:  # Define standard class.
    def __init__(self, first_name, last_name, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.state = state

    def __repr__(self):  # Create repr()
        return f"Person(first_name='{self.first_name}', last_name='{self.last_name}', city='{self.city}', state='{self.state})"

person = Person('Joe', 'Schmoe', 'Schenectady', 'NY')  # Create class instance. Field names, read-write, but much boilerplate
print("class:", person.first_name, person.last_name, "repr:", repr(person))
