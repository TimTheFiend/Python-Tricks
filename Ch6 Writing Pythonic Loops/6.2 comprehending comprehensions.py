squares = [x * x for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""Pseudo-code for squares = [x * x for x in range(10)]
values = [expression for item in collection]
"""

# If you wanted to make this with a for-loop, it'd probably look like this:
squares1 = []
for x in range(10):
    squares1.append(x * x)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares1)
"""Pseudo-code for ^
values = []
for item in collection:
    values.append(expression)
"""

# list comprehension with condition:
even_squares = [x * x for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
"""opposite example:
even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x * x)
"""

"""Same stuff as above but with more readability"""
even_squares = [x * x
                for x in range(10)
                if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Set comprehension:
set_comp = {x * x for x in range(-9, 10)}
print(set_comp)  # {64, 1, 0, 36, 4, 9, 16, 81, 49, 25}

# dictionary comprehension:
dict_comp = {x: x * x for x in range(5)}
print(dict_comp)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
