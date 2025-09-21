import re

my_str = input("Enter String :: ")

x = re.findall("Python", my_str)  # List return
print(x)

if x:
    print("Match Successfully..!!")
else:
    print("Error..!!")