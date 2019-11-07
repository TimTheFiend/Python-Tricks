"""Arrays created with the array.array class are mutable and behave like lists.
except that they are typed arrays, constrained to a single data type.
"""
import array
arr = array.array('f', (1.0, 1.5, 2.0, 2.5))
print(arr[1])   # 1.5
print(arr)      # array('f', (1.0, 1.5, 2.0, 2.5))
del arr[1]
arr.append(1312.0)
try:
    arr[1] = 'oi'
except TypeError:
    print("must be a number")