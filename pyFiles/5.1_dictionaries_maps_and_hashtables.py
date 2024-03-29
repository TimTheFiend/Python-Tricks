#region initial example
phonebook = {
    'andy': 1312,
    'tiffany': 245,
    'fabio': 666,
}
squares = {x: x * x for x in range(6)}
print(phonebook['andy'])    # 1312
print(squares)              # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#endregion

#region Collections.OrderedDict
import collections

d = collections.OrderedDict(one=1, two=2, three=3)
print(d)            # OrderedDict([('one', 1), ('two', 2), ('three', 3)])

d['four'] = 4
print(d)            # OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])
print(d.keys())     # odict_keys(['one', 'two', 'three', 'four'])
print(d.values())   # odict_values([1, 2, 3, 4])
#endregion

#region Collections.ChainMap
from collections import ChainMap

dict1 = {'one': 1, 'two': 2}
dict2 = {'three': 3, 'four': 4}

chain = ChainMap(dict1, dict2)

print(chain) # ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

"""Chainmap searches each collection in the chain
from left to right until it finds the key(or fails)
"""
print(chain['two'], chain['four']) # 2 4
try:
    print(chain['five']) # chain['five'] doesn't exit.
except KeyError:
    print('chain[\'five\'] doesn\'t exit.')
#endregion

#region types.MappingProxyType
"""
This can be helpful if you'd like to return a dictionary
carrying internal state from a class or module,
while discouraging write access to this object.
Using mappingproxytype allows you to put these restrictions in place
without first having to create a full copy of the dictionary.
""" 
from types import MappingProxyType

writable = {'one': 1, 'two': 2}
read_only = MappingProxyType(writable)

print(read_only['one'])
try:
    read_only['one'] = 23 # "Mappingproxy" object does not support item assignment

except TypeError:
    print('"Mappingproxy" object does not support item assignment')
writable['one'] = 42
print(read_only) # {'one': 42, 'two': 2}
#endregion


