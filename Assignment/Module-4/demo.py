import sqlite3

try:
    db = sqlite3.connect("Demo_data.db")
    print("Database Connected Successfully...!")
except Exception as e:
    print(e)

# Create Table

create_tb = "create table product(id integer primary key autoincrement, name text, price integer, qty integer)"

try:
    db.execute(create_tb)
    print("Table Created Successfully...!")
except Exception as e:
    print(e)

# Insert Data

data = int(input("Enter how many records you want to insert: "))    

for i in range(data):
    name = input("Enter Product Name: ")
    price = int(input("Enter Product Price: "))
    qty = int(input("Enter Product Quantity: "))
    print()

    insert_data = f"insert into product(name, price, qty) values ('{name}', {price}, {qty})"

    try:
        db.execute(insert_data)
        db.commit()
        print("Data Inserted Successfully...!")
    except Exception as e:
        print(e)

