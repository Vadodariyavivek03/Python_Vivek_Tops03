import re

my_str = input("Enter String :: ")

# x = re.findall("^Python", my_str)  
# x = re.findall("^[A-Z]", my_str)
x = re.findall("55$", my_str)  
  
print(x)

if x:
    print("Match Successfully..!!")
else:
    print("Error..!!")