side1 = float(input("Enter a first side of triangle"))
side2 = float(input("Enter a second side of triangle"))
side3 = float(input("Enter a third side of triangle"))

if(side1+side2>side3) and (side2+side3>side1) and (side1+side3>side2):
    if(side1==side2==side3):
        print("The triangle is equilateral")
    elif(side1==side2 or side2==side3 or side1==side3):
        print("The triangle is Isosceless")
    else:
        print("The triangle is scalene")