class EnggStudent:
    def __init__(self,sid,name,branch,per):
        self.sid = sid
        self.name = name
        self.branch = branch
        self.per = per

    def show(self):
        print(f"ID:{self.sid }, Name:{self.name}, Branch:{self.branch}, percentage:{self.per}")

    def rank(self):
        if self.per >= 75:
            return "Distinction"
        elif self.per >= 60:
            return "First class"
        elif self.per >= 50:
            return "Second class"
        else:
            return "Fail"
        
sid = int(input("Enter stident ID: "))
name = input("Enter name: ")
branch = input("Enter branch: ")
per = int(input("Enter percentage: "))

s = EnggStudent(sid,name,branch,per)
s.show()
print("Rank:", s.rank())
    
