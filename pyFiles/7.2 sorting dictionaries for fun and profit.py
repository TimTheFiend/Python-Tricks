"""Sorting
"""
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items(), key=lambda x: x[1])) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

"""with operator  
"""
import operator

xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items(), key=operator.itemgetter(1))) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

"""More Lambda
"""
xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items(), key=lambda x: abs(x[1]))) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]


xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items(),
            key=lambda x: x[1],
            reverse=True)) # [('a', 4), ('b', 3), ('c', 2), ('d', 1)]



