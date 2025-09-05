import os

os.chdir("Temp_Data")

x = open("Python_File.txt", "w")

# ----------------------------------------------------- #

id = int(input("Enter an ID : "))
name = input("Enter a Name : ")
age = int(input("Enter an Age : "))
city = input("Enter a City : ")

x.write(f"ID : {id}\n")
x.write(f"Name : {name}\n")
x.write(f"Age : {age}\n")
x.write(f"City : {city}\n")

# ----------------------------------------------------- #

print("Data Written Sucessfully....!!")