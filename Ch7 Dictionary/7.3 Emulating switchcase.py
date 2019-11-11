#region How store function in dictionary and how to call it

"""We can define a function and then store it in a list for later access:"""


def myfunc(a, b):
    return a + b


funcs = [myfunc]
print(str(funcs[0]))  # <function myfunc at 0x000001DF88DE2E50>

print(funcs[0](2, 3))  # 5

#endregion

#region Dictionary like switch/case in pseudo code

# func_dict = {
#     'cond_a': handle_a,
#     'cond_b':
# }

# cond = 'cond_a'
# func_dict[cond]()

#endregion

#region Dictionary like switch/case


def dispatch_if(operator, x, y):
    if operator == 'add':
        return x + y
    if operator == 'sub':
        return x - y
    if operator == 'mul':
        return x * y
    if operator == 'div':
        return x / y


def dispatch_dict(operator, x, y):
    """Makes more sense to have a constant dictionary, and not make one every time.
    """
    return  {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(dispatch_if('mul', 2, 8))     # 16
print(dispatch_dict('mul', 2, 8))   # 16
print(dispatch_if('mal', 2, 8))     # None
print(dispatch_dict('mal', 2, 8))   # None

#endregion
