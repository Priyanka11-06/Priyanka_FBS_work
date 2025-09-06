class Shirt:
    def __init__(self, sid=0, sname= None, stype=None, price=0, size=None):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size

    def __del__(self):
        print(f"Shirt object with id {self.sid} destroyed")

    def showShirt(self):
        print(f"Shirt ID: {self.sid}, Name: {self.sname}, Type: {self.stype}, Size: {self.size}, price: {self.getPrice()}")

    def getPrice(self):
        size_prices = {"small":self.price, "medium": self.price + (self.price*0.10), "large": self.price + (self.price*0.20), "xlarge": self.price + (self.price*0.30) }
        return size_prices.get(self.size.lower(), self.price)
    
s1 = Shirt(101, "Causal Shirt", "Formal", 1000, "small")
s2 = Shirt(301, "Party Shirt", "Causal", 1000, "large")

s1.showShirt()
s2.showShirt()