import re

email = input("Enter Your Email :: ")

x = re.findall('^[a-z0-9]+@+[a-z]+[\.]+[a-z]$', email)

print(x)

if x:
    print("Valid Email..!!")
else:
    print("Error..!!")
