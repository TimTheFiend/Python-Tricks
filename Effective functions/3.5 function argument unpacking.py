def print_vector(x, y, z):
    """Eksempel på "unpacking" af argumenter
    
    Uden at print_vector viser argumenterne kan de stadigvæk hentes.
    Knap så let når det kommer til tuples og lists.
    """
    print('<%s, %s, %s>' % (x, y, z))

tuple_vec = (1, 0, 1)
list_vec = [1, 0, 1]

print_vector(0, 1, 0)
print_vector(tuple_vec[0], tuple_vec[1], tuple_vec[2])
print_vector(list_vec[0], list_vec[1], list_vec[2])

"""Unpacking

Putting a * before an iterable in afunction call will unpack it
and pass its elements as seperate positional arguments to the called function.
"""

print_vector(*tuple_vec)
print_vector(*list_vec)
genexpr = (x * x for x in range(3))
print_vector(*genexpr)

dict_vec = {'y': 0, 'z': 1, 'x': 1}
print_vector(*dict_vec)     # Output: <y, z, x>
"""Dictionaries
Because dictionaries are unordered, this matches up dictionary values
and function arguments based on the dictionary keys:
the x argument recdeives the value assosicated with the 'x' key in the dictionary.
"""
print_vector(**dict_vec)    # Output: <1, 0, 1>