def calc():

    sign = input("Enter a sign (+, -, *, /): ")

    if (sign == '+' or sign == '-' or sign == '*' or sign == '/'):

        n1 = int(input("Enter number 1 : "))
        n2 = int(input("Enter number 2 : "))

        if sign == '+':
            print("Addition : ",n1+n2)
        elif sign == '-':
            print("Substraction : ",n1-n2)
        elif sign == '*':
            print("Multiplication : ",n1*n2)
        elif sign == '/':
            if n2 != 0:
                print("Division : ",n1/n2)
            else:
                print("Error: Division by zero is not allowed.")
    
    else:
        print("Enter valid sign......!")


calc()