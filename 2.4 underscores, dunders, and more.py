# Conventional ways to refer to underscores

def underscore_names():
    # Intended for internal use
    single_leading_underscore = "_var"
    # Intended for avoiding name conflicts with pre-existing names, like class or def.
    single_trailing_underscore = "var_"
    # The interpreter changes the name of the variable in a way that makes it harder to create collisions when the class is extended later
    double_leading_underscore = "__var"
    double_leading_and_trailing_underscore = "__var__"
    single_underscore = "_"

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 42
    
    def __name_mangling_also_applies_to_methods(self):
        print("fuck that's a long ass name")

class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = "overridden"
        self._bar = "overridden"
        self.__baz = "overridden"

def underscores():
    t = Test()
    print(dir(t))
    t2 = ExtendedTest()
    print(t2.foo)
    print(t2._bar)
    try:
        print(t2.__baz) # Gives attributeerror, since the object doesn't have a __baz object, because of the name mangling.
    except AttributeError:
        pass
    print(t2._Test__baz) # works
    t2._Test__name_mangling_also_applies_to_methods()

def what_are_dunders():
    def __this_is_a_dunder__():
        print("__init__ is also a dunder.")

def singe_underscore():
    for _ in range(10):
        if _ == 1:
            print("used to signify temporary varibles, or if they're insignificant.")