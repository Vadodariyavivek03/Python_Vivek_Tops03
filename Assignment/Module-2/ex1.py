obj = ['apple', 'banana', 'cherry', 'mango', 'orange', 'grape', 'kiwi']

print(obj)
print(type(obj))

print(obj[-1])                  # Last element
print(obj[1:4])                 # Elements from index 1 to 3
print(obj[2:])                  # Elements from index 2 to the end
print(obj[:3])                  # First three elements
print(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], sep="\n")      # Print each element on a new line
print(obj[0:6:2])               # Every second element from the index 0 to 5

for i in obj:
    # print(obj.index(i), end="--")  
    # print(i)                        
    print(f"{obj.index(i)}--{i}")       # Print index and value of each element


if 'apple' in obj:                      # using membership operator (in, not in)
    print("Apple is present in list.")
else:
    print("Apple is not present in list.")