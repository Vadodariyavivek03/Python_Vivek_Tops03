# Dictionary ---> ordered, mutable(changeable), no duplicate value, pair{key:value}, {} curly bracket.

my_dict = {
            "id" : 101,
            "name" : "Vivek",
            "age" : 21,
            "city" : "Rajkot"
          }

print(my_dict)
print(type(my_dict))
print(len(my_dict))

print(my_dict["city"])

print(my_dict.get("name"))

print(my_dict.keys())

print(my_dict.values())


# --------------------------------------- #

for i in my_dict:
    print(i)

# --------------------------------------- #

for i in my_dict.values():
    print(i)

# --------------------------------------- #

for i in my_dict.items():
    print(i)

# --------------------------------------- #

for i,j in my_dict.items():
    print(i, "--->", j)

# --------------------------------------- #

for i,j in my_dict.items():
    print(f"Key = {i} and Value = {j}")

# --------------------------------------- #

if 'age' in my_dict:
    print("Yes.....")
else:
    print("No.....")

# --------------------------------------- #

if 104 in my_dict.values():
    print("Yes.....")
else:
    print("No.....")

# --------------------------------------- #

my_dict["country"] = "India"   # Add new pair....

my_dict["id"] = 1001            # Update the dictionary....

print(my_dict)

# --------------------------------------- #

my_dict.pop("age")
my_dict.clear()

print(my_dict)

# --------------------------------------- #

'''obj = my_dict.copy()
print("Copied dict :",obj)'''

# --------------------------------------- #

del my_dict