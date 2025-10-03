import os

os.chdir("Temp_Data")

x = open("Stud_Data.txt", "a")

# ----------------------------------------------------- #

n = int(input("Enter Number of Students : "))

for i in range(n):
    stu_id = int(input("Enter an ID : "))
    stu_name = input("Enter a Name : ")
    stu_age = int(input("Enter an Age : "))
    print("\n----------------------")

    x.write(f"ID : {stu_id}\n")
    x.write(f"Name : {stu_name}\n")
    x.write(f"Age : {stu_age}\n")

    x.write(f"-------------------------------\n")

# ----------------------------------------------------- #

print("Data Written Sucessfully....!!") 