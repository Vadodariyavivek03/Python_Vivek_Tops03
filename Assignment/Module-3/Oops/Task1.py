class stu_info:
    st_id = int(input("Enter ID : "))
    st_name = input("Enter Name : ")
        
    def print_data(self):
        print("Id : ", self.st_id)
        print("Name : ", self.st_name)
        
st = stu_info()
st.print_data()