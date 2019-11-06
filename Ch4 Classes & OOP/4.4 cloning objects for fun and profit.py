"""Shallow Copies er kun en reference til originalen."""
"""En Deep Copy gør at et helt nyt objekt bliver lavet, baseret på originalen."""

"""Making Shallow Copies"""
#region
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)
xs.append(["new sublist"])
print(xs) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
print(ys) # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

xs[1][0] = "x"
print(xs) # Output: [[1, 2, 3], ['x', 5, 6], [7, 8, 9], ['new sublist']]
print(ys) # Output: [[1, 2, 3], ['x', 5, 6], [7, 8, 9]]
#endregion

"""Making Deep Copies"""
#region
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)
# print(xs) #Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(zs) #Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
xs[1][0] = "x"
print(xs) #Output: [[1, 2, 3], ['x', 5, 6], [7, 8, 9]]
print(zs) #Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#endregion

"""Copying Arbitrary Objects"""
#region
#endregion
import copy
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x!r}, {self.y!r})'

# a = Point(13, 12)
# b = copy.copy(a) # Making a shallow copy.
# print(a, b) # Point(13, 12) x2
# print(a is b) # False

"""Class designed to create a more complex object hierarchy"""
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.topleft!r}, {self.bottomright!r})'

rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
print(rect, srect) # Rectangle(Point(0, 1), Point(5, 6)) | Rectangle(Point(0, 1), Point(5, 6))
print(rect is srect) # False

