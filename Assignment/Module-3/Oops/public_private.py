class stud_info:
    # public
    # stu_id = 101
    # stu_name = "Vivek"
    
    # private
    __stu_id = 101
    __stu_name = "Vivek"

    # def getdata(self):                --> # public
    #     print("This is getdata!!")

    def __getdata(self):                # --> private
        print("This is getdata!!")
        print("Id ::",self.__stu_id)
        print("Name ::",self.__stu_name)
    
    def getdata(self):
        self.__getdata()

stu = stud_info()
# print("Id ::",stu.stu_id)
# print("Name ::",stu.stu_name)
# stu.getdata()
# stu._stud_info__getdata()
stu.getdata()