items = {'apple', 'banana', 'cherry', 'mango', 'orange', 'grape', 'kiwi', 'c'}

print(items)
print(type(items))

# --------------------------------------- #

new_set = {'a','b','c','d','e'}
print(new_set)

# --------------------------------------- #

x = items.union(new_set)
print(x)

# --------------------------------------- #

x = items.intersection(new_set)
print(x)

# --------------------------------------- #

x = items.difference(new_set)
print(x)

