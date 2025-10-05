import tkinter
import pymysql

try:
    db = pymysql.connect(host='localhost',user='root',password='',database='task_data')
    print("Database Connected Successfully...!")
except Exception as e:
    print(e)

cr = db.cursor()

# Create Table
tbl_create = "create table stud__info(id integer primary key auto_increment, name varchar(50), city varchar(50))"

try:
    cr.execute(tbl_create)
    print("Table Created Successfully...!")
except Exception as e:
    print(e)

app=tkinter.Tk()
app.title("Database")
app.geometry("300x160")
app.config(bg="light blue")


tkinter.Label(text="Name :",bg="light blue",fg="blue",font='Arial 12 bold').grid(row=0,column=0, sticky="e",padx=8,pady=8)

tkinter.Label(text="City :",bg="light blue",fg="blue",font='Arial 12 bold').grid(row=1,column=0, sticky="e",padx=8,pady=8)

name=tkinter.Entry()
name.grid(row=0,column=1, padx=8,pady=8)
city=tkinter.Entry()
city.grid(row=1,column=1, padx=8,pady=8)

def submit():
    tk_name = name.get()
    tk_city = city.get()

    # Insert Data
    insert_data = f"insert into stud__info(name, city) values('{tk_name}', '{tk_city}')"

    try:
        cr.execute(insert_data)
        db.commit()
        print("Data Inserted Successfully...!")
    except Exception as e:
        print(e)

tkinter.Button(text="Submit",bg="white",fg="green",font='Arial 12 bold',command=submit).grid(row=2,column=0,columnspan=2)

tkinter.mainloop()

