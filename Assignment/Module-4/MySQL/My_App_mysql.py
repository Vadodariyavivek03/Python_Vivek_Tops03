import pymysql

try:
    db = pymysql.connect(host="localhost", user="root", password="", database="python_db")
    print("Database Connected Successfully...!")
except Exception as e:
    print(e)

cr = db.cursor()

# Create Table

tbl_create = "create table product(id integer primary key auto_increment, name varchar(50), price integer, qty integer)"

try:
    cr.execute(tbl_create)
    print("Table Created Successfully...!")
except Exception as e:
    print(e)

# Insert Data

# insert_data = "insert into product(name, price, qty) values ('Laptop', 45000, 2),('Mobile', 15000, 5),('Tablet', 25000, 3)"

# try:
#     cr.execute(insert_data)
#     db.commit()
#     print("Data Inserted Successfully...!")
# except Exception as e:
#     print(e)

# --------------------------------------------------------

# Update Data

# update_data = "update product set name='Earphones', price=4000, qty=5 where id = 3"

# try:
#     cr.execute(update_data)
#     db.commit()
#     print("Data Updated Successfully...!")
# except Exception as e:  
#     print(e)

# --------------------------------------------------------

# Delete Data

# delete_data = "delete from product where id = 3"

# try:
#     cr.execute(delete_data)
#     db.commit()
#     print("Data Deleted Successfully...!")
# except Exception as e:
#     print(e)

# --------------------------------------------------------

# Fetch Data

fetch_data = "select * from product"

try:
    cr.execute(fetch_data)
    data = cr.fetchall()
    # data = cr.fetchmany(2)
    # data = cr.fetchone()
    print(data)
    print("Data Fetched Successfully...!")
except Exception as e:
    print(e)
