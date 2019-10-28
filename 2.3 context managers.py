"""Literally just use the "with" statement
"""
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    """For example, you can use the contextlib.contextmanager decorator to define a generator-based
        factory function for a resource that will then automatically support the with statement.
        Here's what rewriting our ManagedFile context manager exampel with this technique looks like:
    """
    try:
        f = open(name, "w")
        yield f
    finally:
        f.close()

class ManagedFile:
    """What's a context manager?
    It's a simple "protopol" (or interface) that your object needs to follow in order to support the 'with' statement.
    Basically, all you need to do is add __enter__ and __exit__ methods to an object if you want it to function as a context manager.
    Python will call these two methods as the appropriate times in the resource management cycle.
    
    Here's what it might look like.
    """
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        self.file = open(self.name, "w")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# with ManagedFile('hello.txt') as f:
#     f.write('hello world!')
#     f.write('bye')

with managed_file('hello.txt') as f:
    f.write('hello world!')
    f.write('bye')