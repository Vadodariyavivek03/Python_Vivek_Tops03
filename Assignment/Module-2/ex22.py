def fastfood(FullName, Mobile, food_name, food_qty, food_price):
    
    print("\nFastfood Billing App")
    print("====================")

    total = food_qty * food_price
    gst = total * 0.18
    net_total = total + gst

    print(f"\nCustomer Name : {FullName}")
    print(f"Mobile        : {Mobile}")
    print(f"Food          : {food_name}")
    print(f"Quantity      : {food_qty}")
    print(f"Price/item    : Rs.{food_price}")
    print("---------------------------")
    print(f"Total         : Rs.{total}")
    print(f"18% GST       : Rs.{gst}")
    print("============================")
    print(f"Net Total     : Rs.{net_total}")


while True:
    FullName = input("Enter your full name: ")
    if FullName.isalpha():
        break
    else:
        print("Please enter a valid name containing only letters.")
        
while True:
    Mobile = input("Enter your mobile number : ")
    if (Mobile.isdigit() and len(Mobile) == 10):
        break
    else:
        print("Please enter 10 digit valid number......!")


food_name = input("Enter your testy food : ")
food_qty = int(input("Enter food qty : "))      
food_price = float(input("Enter your food price : "))  

fastfood(FullName, Mobile, food_name, food_qty, food_price)

