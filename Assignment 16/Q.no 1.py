class Book:
    count = 0

    def __init__(self, bid=0, bname="unknown", price=0, author=None):  
         self.bid = bid
         self.bname = bname
         self.price = price
         self.author = author
         Book.count += 1

    def __del__(self):
         Book.count -= 1
         print(f"Book object with id {self.bid} destroyed")

    def showBook(self):
         print(f"Book ID: {self.bid}, Name:{self.bname}, price:{self.price}, Author:{self.author}")

    @staticmethod
    def showCount():
         print(f"Total Book Object: {Book.count}")


b1 = Book(101, "Python", 500, "Guido")
b2 = Book(102, "OOP", 600, "Rossum")

b1.showBook()
b2.showBook()
Book.showCount()


    



