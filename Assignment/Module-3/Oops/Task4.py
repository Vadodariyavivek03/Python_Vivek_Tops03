class acc_open:
    acc_number : int
    acc_name : str
    acc_type : str
    acc_bal : int

    def acc_open(self):
        self.acc_number = input("\nEnter your account number : ")
        self.acc_name = input("Enter account holder name : ")
        self.acc_type = input("Enter your account type : ")
        self.acc_bal = 0.0

        print("\nAccount Created Successfully!!\n")

class deposite:
    acc_bal : int
    amount : int

    def deposite(self): 
   
        self.amount = int(input("\nEnter deposite amount (Min 2000) : "))

        if self.amount >= 2000:
            self.acc_bal += self.amount
            print(f"\n{self.amount} Rs. Deposite Successfully !!\n")
        else:
            print("\nError!! Account Minimum Balance should be 2000 Rs.\n")

class cash_withdrwal:
    acc_bal : int
    amount : int

    def cash_withdrwal(self):
    
        self.amount = int(input("\nEnter withdrwal amount : "))

        if self.amount <= self.acc_bal:
            self.acc_bal -= self.amount
            print(f"\n{self.amount} Rs. Cash Withdrawal Successfully !!\n")
        else:
            print("\nError!! Insufficient Balance....\n")

class acc_statement:

    def print_data(self):
        print("\n---------- Account Statement ----------")
        print(f"Account Holder: {self.acc_name}")
        print(f"Account Type  : {self.acc_type}")
        print(f"Account Number: {self.acc_number}")
        print(f"Main Balance  : {self.acc_bal}")
        print("----------------------------------------\n")

class user(acc_open, deposite, cash_withdrwal, acc_statement):

    def choice(self):
        while True:
            print("---------- Banking System ----------")
            print("1. Open Account")
            print("2. Deposit")
            print("3. Cash Withdraw") 
            print("4. Statement")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.acc_open()
            elif choice == "2":
                self.deposite()
            elif choice == "3":
                self.cash_withdrwal()
            elif choice == "4":
                self.print_data()
            elif choice == "5":
                print("Thank you for using our Banking System!!")
                break
            else:
                print("Error!! Invalid Choice, Please! Try Again....")

x = user()
x.choice()

