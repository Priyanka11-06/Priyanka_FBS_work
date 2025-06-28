# To calculate percentage of std based on marks of any 5 subject

Math = int(input("Enter a math marks"))
English = int(input("Enter english marks"))
Phy = int(input("enter a physics marks"))
Che = int(input("enter a chemistry marks"))
Bio= int(input("enter a Biologhy marks"))

total = (Math + English + Che + Bio + Phy)
print("the total marks is =",total)

percentage = total/5
print("The percentage of std is=",percentage)
