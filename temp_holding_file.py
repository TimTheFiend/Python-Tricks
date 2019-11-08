#### TEMPLATE
#region
#endregion

#region Dictionary
""" Dictionaries falls under this category."""
""" Taken directly from the book, since this isn't new """
car1 = {
    'color': 'red',
    'mileage': 3812.4,
    'automatic': True,
    }
car2 = {
    'color': 'blue',
    'mileage': 40231,
    'automatic': False,
    }
# Dicts have a nice repr:
car2 = {'color': 'blue', 'automatic': False, 'mileage': 40231}
# Get mileage:
car2['mileage'] = 40231
# Dicts are mutable:
car2['mileage'] = 12
car2['windshield'] = 'broken'
car2 ={
    'windshield': 'broken',
    'color': 'blue',
    'automatic': False,
    'mileage': 12
    }
# No protection against wrong field names,
# or missing/extra fields:
car3 = {
    'colr': 'green',
    'automatic': False,
    'windshield': 'broken',
    }
#endregion

#region tuple

# Fields: color, mileage, automatic
car1 = ('red', 3812.4, True)
car2 = ('blue', 40231.0, False)
# Tuple instances have a nice repr:
car1 = ('red', 3812.4, True)
car2 = ('blue', 40231.0, False)
# Get mileage:
car2[1] = 40231.0
# Tuples are immutable:
car2[1] = 12
# TypeError: "'tuple' object does not support item assignment"
# No protection against missing/extra fields
# or a wrong order:
car3 = (3431.5, 'green', True, 'silver')

#endregion

#region Writing a custom class - more work, more control

class Car:
    def __init__(self, color, mileage, automatic):
        self.color = color
        self.mileage = mileage
        self.automatic = automatic

car1 = Car('red', 1312, True)
car2 = Car('blue', 666, False)

print(car2.mileage)
car2.mileage = 1312
print(car2.mileage)
#endregion

#region collections.namedtuple
"""Namedtuple objects are implemented as regular python classes internally.
When it coems to memory usage, they are also 'better' than regular classes.
"""
from collections import namedtuple
from sys import getsizeof

p1 = namedtuple('Point', 'x y z')(1, 2, 3)
p2 = (1, 2, 3)

print(getsizeof(p1)) # 64
print(getsizeof(p2)) # 64

Car = namedtuple('Car' , 'color mileage automatic')
car1 = Car('red', 3812.4, True)
print(car1)             # Car(color='red', mileage=3812.4, automatic=True)
print(car1.mileage)     # 3812.4
"""Is immutable
"""

#endregion

#region typing.NamedTuple

#endregion

