#region Initial test with args and kwargs
def testtest(required, *args, **kwargs):
    """Args and Kwargs
    
    required, som navnet forklarer, er krævet for at kunne kalde metoden.
    Args og kwargs er ikke krævet, men kan udfyldes efter behov.

    Vigtig detajle! args og kwargs er en naming convention, og kan fungere med andre navne.
    """
    print(required)
    if args:
        print(args)
    if kwargs:
        print(kwargs)

def testtesttest(x, *args, **kwargs):
    """Here's an example.

    This also gives you an opportunity to modify the arguments before you pass them along.
    """
    kwargs['name'] = 'Alice'
    new_args = args + ('extra', )
    bar(x, *new_args, **kwargs)

try:
    testtest()
except TypeError:
    print("testtest() missing 1 required positional arg: 'required'")
testtest("ay")
testtest("ayy", "lmao")
testtest("ayy", "lmao", "there is no ethical consumption under capitalism.")
testtest("hello", 1, 2, 3, key1='value', key2=999)
# testtest("ayy", "lmao", "there is no ethical consumption under capitalism.", "what he said")
#endregion

#region Class and inheritence with args and kwargs
class Car:
    def __init__(self, color, milage):
        self.color = color
        self.milage = milage

class AlwaysBlueCar(Car):
    """AlwaysBlueCar staying blue
    
    Inde i __init__ sendes argumenterne videre til car, men efter sætter vi farven til blue.
    På den måde så har vi sikret os for at der på ingen måder kan være en anden farve end blue fra klassen.

    Det dårlige ved dette er så at vi ikke ved hvilke argumenter parent-classen forventer.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = "blue"

print(AlwaysBlueCar("green", 42069).color)
print(AlwaysBlueCar("green", 1).color)
#endregion


def trace(f):
    import functools
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        print(f, args, kwargs)
        result = f(*args, **kwargs)
        print(result)
    return decorated_function

@trace
def greet(greeting, name):
    return "{}, {}".format(greeting, name)

greet("Happy Holidays", "dingus")