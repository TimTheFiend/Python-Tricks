#### TEMPLATE
#region
#endregion

"""A set is an unordered collection of objects that does not allow duplicate elements.
"""

# set - your go-to set
vowels = {'a', 'e', 'i', 'o', 'u',}
print('e' in vowels) # True

letters = set('alice')
print(letters.intersection(vowels)) # {'i', 'e', 'a'}

vowels.add('x')
print(vowels) # {'i', 'x', 'u', 'e', 'o', 'a'}

print(len(vowels)) # 6

# frozenset - immutable sets
vowels = frozenset({'a', 'e', 'i', 'o', 'u'})
try:
    vowels.add('p')
except AttributeError:
    print("AttributeError: 'frozenset' object has no attribute 'add'")

# frozensets are hashable and can be used as dictionary keys:
d = { frozenset({1, 2, 3}): 'howdy' }
print(d[frozenset({1, 2, 3})]) # howdy

# collections.Counter - MultiSets
"""The collections.Counter class in the python standard library implements a multiset(bag) type that allows elements in the set to have more than one occurrence.
Which is useful if you need to keep track of not only if an element is part of a set, but also how many times it is included in the set.
"""
from collections import Counter
inventory = Counter()
loot = {'sword': 1, 'The Conquest of Bread': 3}
inventory.update(loot)
print(inventory) # Counter({'The Conquest of Bread': 3, 'sword': 1})

more_loot = {'jc, a bomb': 1, 'A BOMB?': 3, 'sword': 5}
inventory.update(more_loot)
print(inventory) # Counter({'sword': 6, 'The Conquest of Bread': 3, 'A BOMB?': 3, 'jc, a bomb': 1})

print(len(inventory)) # (unique items) output: 4
print(inventory.values()) # (total no. of elements) output: dict_values([6, 3, 1, 3])


