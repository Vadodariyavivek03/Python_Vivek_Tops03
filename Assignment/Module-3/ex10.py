import re

my_str = input("Enter String :: ")

# x = re.findall("[A-Z]", my_str)
# x = re.findall("[a-z]", my_str)
# x = re.findall("[0-9]", my_str)
# x = re.findall("[A-Za-z]", my_str)
x = re.findall("[A-Za-z0-9]", my_str)


print(x)

if x:
    print("Match Successfully..!!")
else:
    print("Error..!!")