import re

my_str = input("Enter String :: ")

x = re.match("Python", my_str) # beginning string
print(x)

if x:
    print("Match Successfully..!!")
else:
    print("Error..!!")