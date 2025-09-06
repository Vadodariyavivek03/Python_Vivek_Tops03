import os
import datetime as dt
import random

os.chdir("Temp_Data")

x = open("Task.txt", "a")

n = int(input("Enter Number of Student Info : "))

for i in range(n):
    stu_name = input("Enter Student Name : ")
    stu_sub = input("Enter Subject Name : ")
    stu_city = input("Enter City Name : ")
    print("\n----------------------")

    x.write(f"Timestemp : {dt.datetime.now()}\n")
    x.write(f"ID : {random.randint(1000,9999)}\n")
    x.write(f"Student Name : {stu_name}\n")
    x.write(f"Subject Name : {stu_sub}\n")  
    x.write(f"City Name : {stu_city}\n")
    x.write(f"-------------------------------\n")

print("Done....!!")
   

