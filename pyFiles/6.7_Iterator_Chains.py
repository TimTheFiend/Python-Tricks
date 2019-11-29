# 1
def integers():
    for i in range(1, 9):
        yield i

chain = integers()
print(list(chain)) # [1, 2, 3, 4, 5, 6, 7, 8]

# 2
def integers():
    for i in range(1, 9):
        yield i

def squared(seq):
    for i in seq:
        yield i * i

chain = squared(integers())
print(list(chain))

# 3
def integers():
    for i in range(1, 9):
        yield i

def squared(seq):
    for i in seq:
        yield i * i

def negated(seq):
    for i in seq:
        yield -i

chain = negated(squared(integers()))
print(list(chain))

# 4
def integers():
    for i in range(1, 9):
        yield i

def squared(seq):
    for i in seq:
        yield i * i

def negated(seq):
    for i in seq:
        yield -i

chain = negated(squared(integers()))
print(list(chain))

"""The data processing happens one element at the time.
There's no buffering between processing steps in the chain:

1. The integers generator yields a single value, let's say 3.
2. This 'activates' the squared generator, which processes the value and passes it on to the next stage as 3x3=9
3. The square number yielded by the squared generator gets fed immediately into the negated generator, which modifies it to -9 and yields it again.
"""