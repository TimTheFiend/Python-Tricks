"""Comparisons of is and ==

The == operator compares by checking for equality:
    If A and B is equal, return True

The is operator compares by identities:
    A and B are different letters, so False
"""
a = [1, 2, 3]
b = a
print(a == b)   # Output: True
print(a is b)   # Output: True

c = list(a)
print(a, b, c)  # Output: [1, 2, 3] [1, 2, 3] [1, 2, 3]

print(a == c)   # Output: True
print(a is c)   # Output: False
"""
C har samme værdier som A, så == er True
C er ikke C, og er derfor False
"""
