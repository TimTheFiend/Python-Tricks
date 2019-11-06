import functools

def uppercase(func):
    """functools

    ved at tilføje @functools.wraps(func) har vi mulighed for at få fat i funcs egen data.
    i uppercase/greet eksempelet printer vi "greet" og greets docstring.
    """
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

@uppercase
def greet():
    """Returns a friendly greeting"""
    return "Hello!"

print(greet.__name__)
print(greet.__doc__)

def lowercase(func):
    """Uden functool
    
    Her bruger vi ikke functool, hvilket gør at greet printer "wrapper", og "None", da wrapper ikke har en docstring.
    """
    def wrapper():
        return func().lower()
    return wrapper

@lowercase
def greet1():
    """Returns a friendly greeting"""
    return "Hello!"

print(greet1.__name__)
print(greet1.__doc__)

