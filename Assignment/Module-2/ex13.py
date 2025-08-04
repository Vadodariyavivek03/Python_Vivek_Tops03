data ={}

n = int(input("Enter how many student : "))

for i in range(n):
    print(f"student {i+1} : ")
    student = input(f"Enter key name {i+1} : ")

    st_data = {}
    pair = int(input("Enter how many pair : "))

    for j in range(pair):
        key = input(f"Enter key {j+1} : ")
        value =input(f"Enter value for {key} : ")
        st_data[key] = value
    
    data[student] = st_data

print("\nData : ",data)