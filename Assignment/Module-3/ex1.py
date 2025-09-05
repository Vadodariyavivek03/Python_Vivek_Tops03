x = open("Data_File.txt", "w")

# ----------------------------------------------------- #

n = int(input("Enter Number : "))

for i in range(1, 11):
    x.write(f" {n} * {i} = {n*i} \n")

# ----------------------------------------------------- #

print("Data Written Sucessfully....!!")