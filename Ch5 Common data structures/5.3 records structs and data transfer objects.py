#region Dictionary
""" Dictionaries falls under this category."""
""" Taken directly from the book, since this isn't new """
car1 = {
    'color': 'red',
    'mileage': 3812.4,
    'automatic': True,
    }
car2 = {
    'color': 'blue',
    'mileage': 40231,
    'automatic': False,
    }
# Dicts have a nice repr:
car2 = {'color': 'blue', 'automatic': False, 'mileage': 40231}
# Get mileage:
car2['mileage'] = 40231
# Dicts are mutable:
car2['mileage'] = 12
car2['windshield'] = 'broken'
car2 ={
    'windshield': 'broken',
    'color': 'blue',
    'automatic': False,
    'mileage': 12
    }
# No protection against wrong field names,
# or missing/extra fields:
car3 = {
    'colr': 'green',
    'automatic': False,
    'windshield': 'broken',
    }
#endregion










