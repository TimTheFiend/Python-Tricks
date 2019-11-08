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


