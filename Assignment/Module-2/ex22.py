def fastfood(name, mobile, food_name, food_qty, food_price):
    
    print("\nFastfood Billing App")
    print("----------------------")

    total = food_qty * food_price
    gst = total * 0.18
    net_total = total + gst

    print(f"\nCustomer Name : {name}")
    print(f"Mobile        : {mobile}")
    print(f"Food          : {food_name}")
    print(f"Quantity      : {food_qty}")
    print(f"Price/item    : Rs.{food_price}")
    print(f"Total         : Rs.{total}")
    print(f"18% GST       : Rs.{gst}")
    print("---------------")
    print(f"Net Total     : Rs.{net_total}")


name = input("Enter Name : ")
mobile = input("Enter mobile number : ")
if not mobile.isdigit():
    print("Enter valid number......!")  

food_name = input("Enter your testy food : ")
food_qty = int(input("Enter food qty : "))      
food_price = float(input("Enter your food price : "))  

fastfood(name, mobile, food_name, food_qty, food_price)

