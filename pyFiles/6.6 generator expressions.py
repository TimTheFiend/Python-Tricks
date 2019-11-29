iterator = ('Hello' for i in range(3))
"""Same as:
def bounded_repeater(value, max_repeats):
    for i in range(max_repeats):
        yield value

iterator = bounded_repeater('Hello', 3)
"""
for x in iterator:
    print(x)
"""Once a generator expression has been consumed, it can't be restarted or reused.
So in some cases there is an advantage to using generator functions or class-based iterators.
"""