class stu_info:     
    st_id = 101                 # Prooperties ---> 3
    st_name = "Vivek"

    def myfunc(self):
       print("This is my function...!!")
    
st = stu_info()

print("Student ID:", st.st_id)
print("Student Name:", st.st_name)
st.myfunc()
