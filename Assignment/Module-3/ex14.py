import re

user_name = input("Enter Your UserName :: ")

x = re.findall('[A-Z]+[a-Z]+[0-9]', user_name)

print(x)

if x:
    print("Valid User_Name..!!")
else:
    print("Error..!!")
