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
"""Younger sibling of the collections.namedtuple"""
from typing import NamedTuple

class Car(NamedTuple):
    color: str
    mileage: float
    automatic: bool

car1 = Car('red', 1312, True)
# Instances have a nice repr:
print(car1)         # Car(color='red', mileage=1312, automatic=True)
print(car1.mileage) # 1312

# Fields are immutable:
try:
    car1.mileage = 12
except AttributeError:
    print("type.NamedTuple")

# Type annotations are not enforced without a separate type checking tool like mypy
print(Car('red', 'NOT_A_FLOAT', 99)) # Car(color='red', mileage='NOT_A_FLOAT', automatic=99)


#endregion

#region struct.Struct - Serialized C Structs

from struct import Struct

my_struct = Struct("i?f")
data = my_struct.pack(23, False, 42.0)

print(data) # b'\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00(B'

print(my_struct.unpack(data)) # (23, False, 42.0)

#endregion


#region types.SimpleNamespace
"""types.SimpleNamespace provides attribute access to its namespace.
This means SimpleNamespace instances expose all of their keys as class attributes.
This means you can use obj.key "dotted" attribute access instead of obj['key']
"""
from types import SimpleNamespace
car1 = SimpleNamespace(color='red', mileage=1312, automatic=True)
# default repr.
print(car1) # namespace(automatic=True, color='red', mileage=1312)

# is mutable
car1.mileage = 12
car1.windshield = 'broken'
del car1.automatic
print(car1) # namespace(color='red', mileage=12, windshield='broken')

#endregion

