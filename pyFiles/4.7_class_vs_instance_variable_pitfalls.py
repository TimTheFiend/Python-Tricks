class Dog:
    num_legs = 4 # <-- Class variable

    def __init__(self, name):
        self.name = name # <-- Instance Variable

j = Dog("Holden")
d = Dog("Caulfield")
print(j.name, d.name)           # Output: Holden Caulfield
print(j.num_legs, d.num_legs, Dog.num_legs)   # Output: 4 4 4
try:
    print(Dog.name)
except AttributeError:
    print("Dog has no attribute 'name'")

j.num_legs = 8
print(j.num_legs, d.num_legs, Dog.num_legs)   # Output: 8 4 4
print(j.num_legs, j.__class__.num_legs)       # Output: 8 4
Dog.num_legs = 6
print(j.num_legs, d.num_legs, Dog.num_legs)   # Output: 8 6 6

"""More practical example of the useful things you can do with class variables
"""
class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1
        # self.num_instances += 1 # Giver en fejl

print(CountedObject.num_instances)      # Output: 0
print(CountedObject().num_instances)    # Output: 1
print(CountedObject().num_instances)    # Output: 2
print(CountedObject.num_instances)      # Output: 2
print(CountedObject().num_instances)    # Output: 3
print(CountedObject().num_instances)    # Output: 4
print(CountedObject.num_instances)      # Output: 4
print(CountedObject().num_instances)    # Output: 5
print(CountedObject().num_instances)    # Output: 6