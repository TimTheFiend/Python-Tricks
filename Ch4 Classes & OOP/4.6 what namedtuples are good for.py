#region Problemstilling
"""
One downside of plain tuples is that the data you store in them can only be pulled out by accessing it through integer indexes.
You can't give names to individual properties stores in a tuple. This can impact code readability.
"""
tup = ('hello', object(), 42)
print(tup)
print(tup[2])
tup[2] = 23 # Output: TypeError: 'tuple' object does not support item assignment

#endregion
#region Namedtuples to the rescue
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')
"""This parameter (Car) is referred to as the "typename" in the python docs.
it's the name of the new class that's being created by calling the namedtuple function.
since namedtuple has no way of knowing what the name of the variable is we're assigning the resulting class to,
we need to explicitly tell it which class name we want to use.
The class name is used in the docstring and the __repr__ implementation that namedtuple automatically generates for us.

What also happens is that inside the second string, 'color milage', a factory function calls split()
on the field names string to parse it into a list of field names. == 'color mileage'.split()
"""
# this is also acceptable, which increases readability.
Car = namedtuple('Car', [
    'color',
    'mileage'
    ])

my_car = Car('red', 1312)
print(my_car.color, my_car[0])     # output: red red
print(my_car.mileage, my_car[1])   # output: 1312 1312
print(tuple(my_car))               # output: ('red', 1312)
# Tuple unpacking and the *-operator work as expected:
color, mileage = my_car
print(color, mileage)              # output: red 1312
print(*my_car)                     # output: red 1312
## Following doesn't work still
# my_car.color = 'blue # attributeerror
#endregion

#region subclassing
"""Since they're built on top of regular python classes you can even add methods to a namedtuple object.
For example, you can extend a numedtuple's class like any other class and add methods and new properties to it that way.
Here's an example.
"""
from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

class MyCarWithmethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithmethods('red', 1312)
print(c.hexcolor())

"""However, this might be a little clunky.
It might be worth doing if you want a class with immutable properties, but it's also easy to shoot yourself in the foot here.
"""
#endregion