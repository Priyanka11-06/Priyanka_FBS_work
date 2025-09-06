class Product:
    def __init__(self,pid=None,pname=None,price=None,quantity=None):
        self.pid=pid
        self.pname=pname
        self.price = price
        self.quantity = quantity
        print("Product object created")

    def showProduct(self):
        print("....product details...")
        print("product ID:",self.pid)
        print("product Name:",self.pname)
        print("product price:",self.price)
        print("product Quantity:",self.quantity)


def __del__(self):
    print("Product object destroyed")

p1 = Product()
p1.showProduct()

p2 = Product(202,"Laptop",55000,10)
p2.showProduct()