class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        """Inspecting my_car in an interpreter session still gives the <__main__.Car object at 0x00000227F7A39880> output"""
        return f'a {self.color} car'


my_car = Car('Red', 1312)
print(my_car)                           # Pre-__str__ Output: <__main__.Car object at 0x000002A8C5FA9880>
print(my_car.color, my_car.mileage)     # Output: Red 1312
print(my_car)                           # Post-__str__ Output: a Red car
