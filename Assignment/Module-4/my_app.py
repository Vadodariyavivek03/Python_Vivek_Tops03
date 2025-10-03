import sqlite3

try:
    db = sqlite3.connect("my_database.db")
    print("Database Connected!!")
except Exception as e:
    print(e)

# Create Table

tbl_create = "create table users(id integer primary key autoincrement, name text, city text)"

try:
    db.execute(tbl_create)
    print("Table Created!!")
except Exception as e:
    print(e)

# Insert Data

# insert_data ='''insert into users(name, city) values
# ('Vivek', 'Rajkot'),
# ('Meet', 'Ahmedabad'),
# ('Kishan', 'Surat'),
# ('Jay', 'Vadodara'),
# ('Parth', 'Gandhinagar')'''

# try:
#     db.execute(insert_data)
#     db.commit()
#     print("Data Inserted!!")
# except Exception as e:
#     print(e)

# Update Data

update_data = "update users set name='Kashyap', city='Mumbai' where id=4"

try:
    db.execute(update_data)
    db.commit()
    print("Data Updated!!")
except Exception as e:
    print(e)

# Delete Data

delete_data = "delete from users where id=5"

try:
    db.execute(delete_data)
    db.commit()
    print("Data Deleted!!")
except Exception as e:
    print(e)

# Fetch Data

cr = db.cursor()
fetch_data = "select * from users"
try:
    cr.execute(fetch_data)
    data = cr.fetchall()
    # data = cr.fetchone()  # for single row
    # data = cr.fetchmany(3)  # for multiple rows
    for i in data:
        print(i)
except Exception as e:
    print(e)