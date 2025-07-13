a1 = float(input("Enter 1st side of triangle"))
a2 = float(input("Enter 2nd side of triangle"))
a3 = float(input("Enter 3rd side of triangle"))

if(a1+a2>a3 and a1+a3>a2 and a2+a3>a1):
    print("Triangle is valide")
else:
    print("Triangle is invalid")