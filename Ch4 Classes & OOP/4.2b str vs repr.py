#region
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return '__repr__ for Car'
    
    def __str__(self):
        return '__str__ for Car'

my_car = Car('red', 1312)
print(my_car)           # Output: __str__ for Car
print(str([my_car]))    # Output: [__repr__ for Car]
#endregion

import datetime
today = datetime.date.today()

print(str(today)) # Output: 2019-11-06
print(repr(today)) # Output: datetime.date(2019, 11, 6)

class Car1:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        """Please note that I'm using the !r conversion flag to make sure the output string uses repr(self.x) instead of str(self.x)
        """
        #return f'Car1({self.color!r}, {self.mileage!r})'
        # Don't repeat Yourself principle:
        return(f'{self.__class__.__name__}({self.color!r}, {self.mileage!r})')

print(repr(Car1("Hot-pink", 1312))) # Output: Car1('Hot-pink', 1312)
