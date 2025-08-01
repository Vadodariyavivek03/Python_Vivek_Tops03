State = ()

n = int(input("Enter number of states: "))

for i in range(n):
    x = input(f"Enter state name {i+1}: ")
    State += (x,) 

print(State)

# print(tuple(State)) 