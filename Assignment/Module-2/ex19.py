def stinfo(n1, n2):
    print("id : ",n1)
    print("name : ",n2)

n = int(input("Enter how many student : "))

info = []

for i in range(n):
    print(f"\nstudent {i+1} : ")
    n1 = int(input("Enter id : "))
    n2 = input("Enter name : ")
    info.append((n1,n2))

print("\nAll Student Data:")

count = 1
for n1, n2 in info:
    print(f"\nStudent {count}:")
    stinfo(n1,n2)
    print("-------------------")
    count += 1
    

