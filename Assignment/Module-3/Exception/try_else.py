try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))

    print("Sum : ", a + b)

except Exception as e:
    print(e)

else:
    # print("This is Else Block....!!")
    print("Mul : ", a * b)


