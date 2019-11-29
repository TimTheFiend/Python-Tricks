lst = [1, 2, 3, 4, 5]
print(lst[1:3:1]) # [start:stop:step] OUTPUT: [2, 3]
print(lst[::2]) # called a 'stride' OUTPUT [1, 3, 5]
print(lst[::-1]) # [5, 4, 3, 2, 1]

"""You can use the :-operator to clear all elements from a list without destroying the list object itself.
"""
lst = [1, 2, 3, 4, 5]
del lst[:] 
print(lst) # []
""" IS THE SAME AS """
lst.clear()

"""replacing all elements without creating new object
"""
lst = [1, 2, 3, 4, 5]
original_lst = lst
lst[:] = [7, 8, 9]
print(str(lst)) # [7, 8, 9]
print(str(original_lst))
print(original_lst is lst) # True

"""Also used for creating shallow copies """
copied_lst = lst[:]
print(str(copied_lst)) # [7, 8, 9]
print(copied_lst is lst) # False
