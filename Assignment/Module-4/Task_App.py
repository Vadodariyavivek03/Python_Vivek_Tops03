import sqlite3

try:
    db = sqlite3.connect("temp_data.db")
    print("Database Connected!!")
except Exception as e:
    print(e)

# Create Table

tbl_create = "create table stud_info(id integer primary key autoincrement, name text, city text, sub text, marks integer)"

try:
    db.execute(tbl_create)
    print("Table Created!!")
except Exception as e:
    print(e)

# Insert Data

# n = int(input("Enter how many records insert :: ")) 

# for i in range(n):
    
#     name = input("Enter Name :: ")
#     city = input("Enter City :: ")
#     sub = input("Enter Subject :: ")
#     marks = int(input("Enter Marks :: "))

#     insert_data = f"insert into stud_info(name, city, sub, marks) values ('{name}', '{city}', '{sub}', {marks})"

#     try:
#         db.execute(insert_data)
#         db.commit()
#         print("Data Inserted!!")
#     except Exception as e:
#         print(e)

# Update Data

# id = int(input("Enter ID which you want to update :: "))

# column = input("Enter column name which you want to update :: ")
# value = input("Enter Value :: ")

# update_data = f"update stud_info set {column}='{value}' where id=.{id}"

# try:
#     db.execute(update_data)
#     db.commit()
#     print("Data Updated!!")
# except Exception as e:
#     print(e)

# Delete Data

id = int(input("Enter ID which you want to delete :: "))

delete_data = f"delete from stud_info where id={id}"

try:
    db.execute(delete_data)
    db.commit()
    print("Data Deleted!!")
except Exception as e:
    print(e)




