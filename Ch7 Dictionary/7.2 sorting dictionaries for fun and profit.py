xs = {'a': 4, 'c': 2, 'b': 3, 'd': 1}
print(sorted(xs.items(), key=lambda x: x[1])) # [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
