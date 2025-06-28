# Find the root of Quadratic Equation

a=int(input("enter  a value of a"))
b= int(input("enter a vaiue of b"))
c= int(input("enter a value of c"))

ans = (b*b) - (4*a*c)
ans = ans ** 0.5
root1 = (-b+ ans)/ (2*a)
root2 = (-b- ans)/ (2*a)
print("root1=",root1)
print("root2=",root2)