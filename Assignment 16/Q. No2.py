class Product:
    dis = 0

    def __init__(self, pid=0, pname=None, price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def __del__(self):
        print(f"product object with id {self.pid} destroyed")

    def showProduct(self):
        print(f"product ID: {self.pid}, Name: {self.pname}, price: {self.price}, Quantity: {self.quantity}")

    def applyDiscount(self):
        discounted_price = self.price - (self.price * Product.dis / 100)
        print(f"Discounted price of {self.pname}: {discounted_price}")

p1 = Product(201, "Laptop", 50000, 5)
p1.showProduct()
p1.applyDiscount()

