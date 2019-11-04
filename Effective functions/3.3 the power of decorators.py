"""
Decorators "decorate" or "wrap" another function and let you execute code before and after the wrapped function runs.
decorators allows you to define reusable building blocks that can change or extend the behavior of other functions.
And, they let you do that without permanently modifying the wrapped function itself.
The fucntions behavior changes only when it's decorated.
"""
"""
Putting an @null_decorator line in front of the function definition is the same as defining the function 
and then running through the decorator.
"""
"""
Instead of explicitly calling null_decorator on greet and then reassigning the greet variable,
you can use python's @ syntax for decorating a function more conveniently:
"""
def null_decorator(func):
    return func
 #region Useless Decorators

def greet():
    return "hello"

@null_decorator
def greet1():
    return "hello"

# greet = null_decorator(greet)
# print(greet())
# print(greet1())

#endregion

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet2():
    return "howdy"

print(greet2())