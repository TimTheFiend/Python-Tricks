"""Dette er ting du allerede ved, emnet er 2 sider langt.

Python adds an implicit return None statement to the end of any function.
Default return value is None.
"""
def foo1(value):
    if value:
        return value
    else:
        return None

def foo2(value):
    """Bare return statement implies 'return None'"""
    if value:
        return value
    else:
        return

def foo3(value):
    """Missing return statement implies 'return None'"""
    if value:
        return value