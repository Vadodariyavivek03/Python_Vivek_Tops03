class vivek:
    vk_id : int
    vk_tech : str
    
    def v_get_data(self):
        self.vk_id = int(input("Enter ID : "))
        self.vk_tech = input("Enter Technology : ")

class meet:
    mt_id : int
    mt_tech : str
    
    def m_get_data(self):
        self.mt_id = int(input("\nEnter ID : "))
        self.mt_tech = input("Enter Technology : ")

class kashyap:
    kp_id : int
    kp_tech : str
    
    def k_get_data(self):
        self.kp_id = int(input("\nEnter ID : "))
        self.kp_tech = input("Enter Technology : ")

class tops(vivek, meet, kashyap):

    def print_data(self):

        print("\nId ::",self.vk_id)
        print("Technology ::",self.vk_tech)

        print(f"{"-" * 40}")
        print("Id ::",self.mt_id)
        print("Technology ::",self.mt_tech)

        print(f"{"-" * 40}")
        print("Id ::",self.kp_id)
        print("Technology ::",self.kp_tech)

tp = tops()
tp.v_get_data()
tp.m_get_data()
tp.k_get_data()
tp.print_data()