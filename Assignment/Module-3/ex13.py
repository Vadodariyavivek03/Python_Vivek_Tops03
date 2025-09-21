import re

my_str = input("Enter String :: ")

# x = re.findall("\w", my_str)  
# x = re.findall("\W", my_str)  # None of word
# x = re.findall("\s", my_str)  
# x = re.findall("\S", my_str)  
# x = re.findall("\d", my_str)
# x = re.findall("\D", my_str)  
# x = re.findall(r"\bThis", my_str)  
# x = re.findall(r"\B895", my_str)  # end
# x = re.findall("\APython", my_str)  
x = re.findall("009\Z", my_str)  
  
print(x)

if x:
    print("Match Successfully..!!")
else:
    print("Error..!!")