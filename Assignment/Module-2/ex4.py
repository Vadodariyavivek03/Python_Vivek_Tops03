# Tuple --> ordered, unmutable(unchangeble), allow duplicate values, () round bracket.

obj = ('apple', 'banana', 'cherry', 'mango', 'orange', 'grape', 'kiwi', 'watermelon', 'peach', 'pomegranate')

print(obj)

print(type(obj))

print(obj[0])

print(obj[2:9])

print(obj[:4])

print(obj[1:7:2])

print(obj[-1])

print(len(obj))

#---------------------------------------#

for i in obj:
    print(i)

#---------------------------------------#

if 'pear' in obj:
    print("Yes........")
else:
    print("No.........")

#---------------------------------------#

print(obj.index("watermelon"))

#---------------------------------------#

del obj

#---------------------------------------#

tuple1 = (1, 2, 6, 8, 4)
tuple2 = (3, 5, 7, 10, 14)

x = tuple1 + tuple2

print(x)