import tkinter

screen = tkinter.Tk()

screen.title("My Tkinter App")
screen.geometry("400x400")
screen.config(background="light blue")

tkinter.Label(text="First Name :", bg="light blue", fg="orange", 
              font=("Arial 10 bold")).grid(row=0, column=0, sticky="w")
tkinter.Label(text="Last Name :", bg="light blue", fg="orange", 
              font=("Arial 10 bold")).grid(row=1, column=0, sticky="w")
tkinter.Label(text="E-mail :", bg="light blue", fg="orange", 
              font=("Arial 10 bold")).grid(row=2, column=0, sticky="w")
tkinter.Label(text="Mobile :", bg="light blue", fg="orange", 
              font=("Arial 10 bold")).grid(row=3, column=0, sticky="w")

tkinter.Entry().grid(row=0, column=1, sticky="w")
tkinter.Entry().grid(row=1, column=1, sticky="w")
tkinter.Entry().grid(row=2, column=1, sticky="w")
tkinter.Entry().grid(row=3, column=1, sticky="w")

tkinter.Radiobutton(value=1, text="Male", bg="light blue", fg="orange", 
                    font=("Arial 10 bold")).grid(row=4, column=0, sticky="w")
tkinter.Radiobutton(value=2, text="Female", bg="light blue", fg="orange", 
                    font=("Arial 10 bold")).grid(row=4, column=1, sticky="w")

tkinter.Checkbutton(text="Gujrati", bg="light blue", fg="orange", 
                    font=("Arial 10 bold")).grid(row=5, column=0, sticky="w")
tkinter.Checkbutton(text="Hindi", bg="light blue", fg="orange", 
                    font=("Arial 10 bold")).grid(row=6, column=0, sticky="w")
tkinter.Checkbutton(text="English", bg="light blue", fg="orange", 
                    font=("Arial 10 bold")).grid(row=7, column=0, sticky="w")

tkinter.Button(text="Submit", bg="green", fg="white", font=("Arial 10 bold")).place(x=150, y=250)
screen.mainloop()