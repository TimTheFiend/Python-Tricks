"""In this chapter you'll see how to write several python classes that support the iterator protocol.
They'll serve as "non-magical" examples and test implemtations you can build upon and deepen your understanding with.
"""

"""Iterating forever"""
class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self, source):
        """We link each RepeaterIterator instance to the Repeater object that created it.
        That way we can hold onto the "source" that's being iterated over.
        """
        self.source = source
    
    def __next__(self):
        """We reach back into the "source" Repeater instance and return the value associated with it.
        """
        return self.source.value

repeater = Repeater("OI!")
for item in repeater:
    print(item)

"""A simple Iterator class"""
class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value

repeater = Repeater("You're the man now, dawg.")
for item in repeater:
    print(item)

"""Who wants to iterate forever?"""
# numbers = [1, 2, 3]
# for n in numbers:
#     print(n) # NEVER STOPS

my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # StopIteration Exception

"""A class that stops iterating after a set number of repetitions:"""
class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

bounded_repeater = BoundedRepeater("Whoah", 3)
for item in bounded_repeater:
    print(item) # 3x Whoah

repeater = BoundedRepeater("hello", 3)
iterator = iter(repeater)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        break
    print(item) # 3x Hello
