class master:
    def header(self, home, about, contact):
        print("Home ::",home)
        print("About ::",about)
        print("Contact ::",contact)

class index(master):
    def header(self, home, about, contact):
        return super().header(home, about, contact)
    
class profile(master):
    def header(self, home, about, contact):
        return super().header(home, about, contact)
    
ind = index()
ind.header("Home", "About", "Contact")