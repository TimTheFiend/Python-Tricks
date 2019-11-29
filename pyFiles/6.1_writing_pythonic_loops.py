# Example of non-pythonic loop
my_items = ['a', 'b', 'c']
i = 0
while i < len(my_items):
    print(my_items[i])
    i += 1
"""
1) It keeps track of the index i manually. (Initializing, and incrementing)
2) It uses len() to get the size of the array container in order to determine how often to iterate.
"""

# This is better, but not very pythonic.
my_items = ['a', 'b', 'c']
for i in range(len(my_items)):
    print(my_items[i])

# Example of Pythonic loop
my_items = ['a', 'b', 'c']
for item in my_items:
    print(item)

# Example if you need the item index.
my_items = ['a', 'b', 'c']
for i, item in enumerate(my_items):
    print(f'{i}: {item}')

# Iterators in python can return more than just one value.
# they can return tuples with an arbitrary number of values that can then be unpacked.
emails = {
    'bob': '@yahoo.com',
    'kaiser': '@gmail.com'
}
for name, email in emails.items():
    print(f"{name}, {email}")

"""What if you absolutely need a c-style loop?"""
# for (int i = a; i < n; i += s) {
#     // code goes here
# }

"""How would ^ translate to python?
the range function comes to our rescue again,
it accepts optional parameters to control the start value for the loop (a),
the stop value (n), and the stepsize (s)
"""
a, n, s = 0, 10, 1
for i in range(a, n, s):
    print("it should do something.")