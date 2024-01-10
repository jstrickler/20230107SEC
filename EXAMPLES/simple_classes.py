x = list()     #   list x = new list();
x.append('hello')
x.insert(0, "wombat")
y = list()
y.append('a')
y.append('b')


class Mammal:
    def run(self):
        print("running...")

class Dog(Mammal):
    def bark(self):
        print("woof woof")



class FilingsBase:
    pass
    # name
    # contact info
    # address 
    # ????


class USFilings(FilingsBase):
    pass
    # 10K, 10Q, 8K

class ForeignFilings(FilingsBase):
    pass
    # 20F, 6K, ???

if __name__ == "__main__":
    d1 = Dog()
    print(f"{type(d1) = }")

    d1.bark()  #  Dog.bark(d1)
    d1.run()
    print(f"{type(list) = }")
    print(f"{type(x) = }")
