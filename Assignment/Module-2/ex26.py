acc_holder = ""
acc_type = ""
acc_number = ""
balance = 0.0

def acc_open():
    global acc_holder, acc_type, acc_number, balance

    new_acc_number = input("\nEnter your account number : ")
    
    if new_acc_number == acc_number:
        print("\nError!! Account number already exists.. Try again....!!\n")
        return

    acc_holder = input("Enter account holder name : ")
    acc_type = input("Enter your account type : ")
    acc_number = new_acc_number
    balance = 0.0

    print("\nAccount Created Successfully!!\n")


def deposite():
    global balance

    amount = float(input("\nEnter deposite amount (Min 2000) : "))

    if amount >= 2000:
        balance += amount
        print(f"\n{amount} Rs. Deposite Successfully !!\n")
    else:
        print("\nError!! Account Minimum Balance should be 2000 Rs.\n")


def cash_withdrwal():
    global balance

    amount = float(input("\nEnter withdrwal amount : "))

    if amount <= balance:
        balance -= amount
        print(f"\n{amount} Rs. Cash Withdrawal Successfully !!\n")
    else:
        print("\nError!! Insufficient Balance....\n")


def acc_statement():
    global acc_holder, acc_type, acc_number, balance

    print("\n---------- Account Statement ----------")
    print(f"Account Holder: {acc_holder}")
    print(f"Account Type  : {acc_type}")
    print(f"Account Number: {acc_number}")
    print(f"Main Balance  : {balance}")
    print("----------------------------------------\n")


while True:
    print("---------- Banking System ----------")
    print("1. Open Account")
    print("2. Deposit")
    print("3. Cash Withdraw") 
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc_open()
    elif choice == "2":
        deposite()
    elif choice == "3":
        cash_withdrwal()
    elif choice == "4":
        acc_statement()
    elif choice == "5":
        print("Thank you for using our Banking System!!")
        break
    else:
        print("Error!! Invalid Choice, Please! Try Again....")
















        