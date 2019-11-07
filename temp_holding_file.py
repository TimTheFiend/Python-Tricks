#### TEMPLATE
#region
#endregion

#region list - mutable dynamic arrays 
arr = ['one', 'two', 'three']
print(arr[0]) # one
# arrays also have an repr
print(arr)
# mutable
arr[1] = 'ayy'
del arr[2]
arr.append(23)
#endregion

#region tuple - immutable containers
arr = 'one', 'two', 'three'
print(arr[0]) # one

# repr
print(arr)

# immutable
arr[1] = 'hello' # TypeError
del arr[2]       # TypeError
arr.append(23)   # ('one', 'two', 'three', 23)
#endregion

#region array.array - basic typed arrays

#endregion


