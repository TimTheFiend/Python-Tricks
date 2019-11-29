#region initial example
class MyClass:
    def method(self):
        """Instance method:
        Is a regular instance method, I.E. the basic method type.
        Requires self which points to MyClass.
        """
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        """Class method:
        Instead of accepting a self parameter, class methods take a cls pararmeter that points to the class -
        and not the object instance- when the method is called.
        Since the class method only has access to this cls argument, it can't modify object instance state.
        That would require access to self.
        However, class methods can still modify class state that applies across all instances of the class.
        """
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():
        """Statid method
        This type of method doesn't take a self or a cls parameter, although it can be made to accept parameter(s).
        As a result, it cannot modify object or class state.
        Static methods are restricted in what data they can access.
        
        Returns:
            [type] -- [description]
        """
        return 'static method called'

obj = MyClass()
print(obj.method())         # ('instance method called', <__main__.MyClass object at 0x0000021419CCAE50>)
print(MyClass.method(obj))  # ('instance method called', <__main__.MyClass object at 0x00000251ADFEAE50>)
print(obj.classmethod())    # ('class method called', <class '__main__.MyClass'>)
print(obj.staticmethod())   # static method called

print(MyClass.classmethod())    # ('class method called', <class '__main__.MyClass'>)
print(MyClass.staticmethod())   # static method called
try:
    print(MyClass.method())   # static method called
except TypeError:
    print("Unbound method method() must be called with MyClass isntance as first argument (got nothing instead)")
#endregion

#region Pizza example
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self):
        return f"Pizza({self.ingredients!r})"
    
    """Factory function:
    a factory is an object for creating other objects – formally a factory is a function or method
    that returns objects of a varying prototype or class[1] from some method call, which is assumed to be "new".
    Source: https://en.wikipedia.org/wiki/Factory_(object-oriented_programming)

    Python only allows one __init__ method per class.
    Using class methods makes it possible to add as many alternative constructors as necessary
    """
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])
    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])

print(Pizza(["Coffee", "Cheetos"])) # Pizza(['Coffee', 'Cheetos'])
print(Pizza(["Coffee", "Cheetos", "Chicken"])) # Pizza(['Coffee', 'Cheetos', 'Chicken'])
print(Pizza(["Coffee"] * 4 )) # Pizza(['Coffee', 'Coffee', 'Coffee', 'Coffee'])
margh = Pizza.margherita()
print(Pizza.margherita(), margh) # Pizza(['mozzarella', 'tomatoes']) Pizza(['mozzarella', 'tomatoes'])
print(Pizza.prosciutto())        # Pizza(['mozzarella', 'tomatoes', 'ham'])
#endregion

#region when to use static methods
#endregion

import math
class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients
    def __repr__(self):
        print(f'Pizza({self.radius!r}, {self.ingredients!r})')
    
    def area(self):
        print(self.circle_area(self.radius))
    
    @staticmethod
    def circle_area(r):
        return r ** 2 * math.pi
    
p = Pizza(4, ['Coffee', 'Cheetos'])
p.__repr__() # Pizza(4, ['Coffee', 'Cheetos'])
p.area()                        # 50.26548245743669
print(Pizza.circle_area(4))     # 50.26548245743669