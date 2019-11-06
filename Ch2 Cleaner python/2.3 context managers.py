"""Literally just use the "with" statement
"""
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    """For example, you can use the contextlib.contextmanager decorator to define a generator-based
        factory function for a resource that will then automatically support the with statement.
        Here's what rewriting our ManagedFile context manager exampel with this technique looks like:

        In this case, managed_file() is a generator that first acquires the resource.
        After that, it temporarily suspends its own execution and yields the resource so it can be used by the caller.
        When the caller leaves the with context, the generator continues to execute so that any remaining
        clean-up steps can occur and the resource can get released back to the system.
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

class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):
        self.level += 1
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)

def indenter_as_context_manager():
    with Indenter() as indent:
        indent.print("hi")
        with indent:
            indent.print("howdy")
            with indent:
                indent.print("Yeehaw")
        indent.print("every modern american president is a war criminal.")


#region VALG AF METHOD AT KØRER
what_function_to_run = int(input("Hvilken function vil du kører? "))
if what_function_to_run == 1:
    with ManagedFile('hello.txt') as f:
        f.write('hello world!')
        f.write('bye')
elif what_function_to_run == 2:
    with managed_file('hello.txt') as f:
        f.write('hello world!')
        f.write('bye')
elif what_function_to_run == 3:
    indenter_as_context_manager()
else:
    print("Ya didn't change it")
#endregion