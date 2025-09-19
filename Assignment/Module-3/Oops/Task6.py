import requests

class Check_Net:

    def __init__(self):
        self.check_internet()

    def check_internet(self):
        
        try:
            requests.get("https://www.google.com")
            print("Internet is ON....!!")

        except:
            print("Internet is OFF....!!")

x = Check_Net()
