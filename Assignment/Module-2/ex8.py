data = {}

n = int(input("Enter how many number of pair you want to add : "))

for i in range(n):
    key = input(f"Enter key {i+1} : ")
    value =input(f"Enter value for {key} : ")
    data[key] = value

print("Data : ",data)