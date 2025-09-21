import re

my_str = input("Enter String :: ")

x = re.findall("Py..on", my_str)  # Restriction 
# x = re.findall("This|That", my_str)  

print(x)

if x:
    print("Match Successfully..!!")
else:
    print("Error..!!")
