from abc import ABCMeta, abstractmethod
# Abstract Base Class (ABC)

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        return 'foo() called'

concrete = Concrete() # Output: TypeError: Can't instantiate abstract class Concrete with abstract methods bar
"""Da klassen Concrete ikke har implementeret en bar() giver dette en fejl, da abstract classes kræver alle metoder.
Uden ABC og @abstractmethod ville vi kun få en "NotImplementedError", og ikke specifikt hvad der mangler.
"""