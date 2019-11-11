class Repeater:
    def __init__(self, value):
        self.value = value
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.value

def repeater(value):
    """'If I rewrite this iterator class as a generator, it looks like this:

    How generators work:
    Calling a generator function doesn't even run the function, it merely creates and returns a generator object:
    
    """
    while True:
        yield value

for x in repeater("hi"):
    print(x) # Infinite loop


"""Generators that stop generating."""
def repeat_three_times(value):
    """Generators stop generating values as soon as control flow returns
    from the generator function by any means other than a yield statement.
    This means you no longer have to worry about raising StopIteration at all!
    """
    yield value
    yield value
    yield value

for x in repeat_three_times('Hello there.'):
    print(x) # 3x Hello There.

"""Re-implementing BoundedRepeater as a generator function.
"""
def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value

for n in bounded_repeater("YOU!", 5):
    print(n) # 5x YOU!

"""More simplifying!"""
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value
