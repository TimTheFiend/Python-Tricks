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
#endregion