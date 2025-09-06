class Shirt:
    def __init__(self,sid=None,sname=None,stype=None,price=None,size=None):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size
        print("Shirt object created")

    def showShirt(self):
        print(" shirt details ")
        print("shirt Id :",self.sid)
        print("shirt name:", self.sname)
        print("Type :", self.stype)
        print("Size:", self.size)

    def __del__(self):
        print("shirt object destroyed")

s1 = Shirt()
s1.showShirt()

s2 = Shirt(301,"peter england", "Foraml", 1200, "large")
s2.showShirt()