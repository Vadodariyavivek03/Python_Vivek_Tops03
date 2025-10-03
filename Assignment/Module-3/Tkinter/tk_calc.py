import tkinter

app=tkinter.Tk()
app.title("Calculator")
app.geometry("400x400")
app.config(bg="light blue")


tkinter.Label(text="Number 1 :",bg="light blue",fg="blue",font='Arial 15 bold').grid(row=0,column=0)

tkinter.Label(text="Number 2 :",bg="light blue",fg="blue",font='Arial 15 bold').grid(row=1,column=0)

n1=tkinter.Entry()
n1.grid(row=0,column=1)
n2=tkinter.Entry()
n2.grid(row=1,column=1)

def add():
    result = n1 + n2
    print("Addition :",result.get())
    
def sub():
    result = n1 - n2
    print("Substraction :",result)

def mul():
    result = n1 * n2
    print("Product :",result)

def div():
    result = n1 / n2
    print("Division :",result)

tkinter.Button(text="Addition",fg="blue",font='Arial 15 bold',command=add).place(x=100,y=100)

tkinter.Button(text="Substraction",fg="red",font='Arial 15 bold',command=sub).place(x=200,y=100)

tkinter.Button(text="Multiplication",fg="green",font='Arial 15 bold',command=mul).place(x=300,y=100)

tkinter.Button(text="Division",fg="orange",font='Arial 15 bold',command=div).place(x=400,y=100)





tkinter.mainloop()