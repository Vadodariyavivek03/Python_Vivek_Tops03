import os

os.chdir("Adv_Python\Python_data")

# ----------------------------------------------------- #

x = open("Coding1.txt", "w")

# ----------------------------------------------------- #

n = int(input("Enter Number : "))

for i in range(n):
    x.write(f"{i+1} \n")

# ----------------------------------------------------- #

print("Data Written Sucessfully....!!")