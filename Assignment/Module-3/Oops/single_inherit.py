class stud_info:
    st_id : int
    st_name : str

    def get_data(self):
        self.st_id = int(input("Enter ID : "))
        self.st_name = input("Enter Name : ")

class result(stud_info):

    def print_data(self):
        print("Id : ", self.st_id)
        print("Name : ", self.st_name)
                               
rs = result()
rs.get_data()

rs.print_data()