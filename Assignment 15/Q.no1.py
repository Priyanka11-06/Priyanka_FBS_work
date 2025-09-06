class Book:
    def __init__(self,bid=0, bname="NA",price=0,author="unknown"):
        self.bid = bid
        self.bname = bname 
        self.price = price
        self.author = author
        print("Book object created")

    def __del__(self):
        print("Book object Destroyed")

    def showBook(self):
        print(f"Book ID:{self.bid}, Name:{self.bname}, price{self.price}, Author:{self.author}")

print("\n...Using default constructor ")
b1 = Book()
b1.showBook()

print("\n....Using parameterized constructor")
b2 = Book(105,"python",500,"Guido van Rossum")
b2.showBook()
