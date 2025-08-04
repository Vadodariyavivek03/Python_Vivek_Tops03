# Set ---> unordered, unindexed, no duplicate values, {} curly bracket.

items = {'apple', 'banana', 'cherry', 'mango', 'orange', 'grape', 'kiwi'}

print(items)
print(type(items))

print(len(items))

# --------------------------------------- #

for i in items:
    print(i)

# --------------------------------------- #

if 'kiwi' in items:
    print("Yes.....")
else:
    print("No.....")

# --------------------------------------- #

items.add('pear')
print(items)

# --------------------------------------- #

items.update(['watermelon', 'blueberry', 'peach', 'pomogranate'])   # add multiple values or another set.
print(items)

# --------------------------------------- #

items.remove('kiwi')
print(items)

# --------------------------------------- #

items.pop()
print(items)

# --------------------------------------- #

'''items.pop(2)                 This line give error because set is unindexed. so, that is not possible.
print(items)'''

# --------------------------------------- #

items.clear()
print(items)

# --------------------------------------- #

del items



