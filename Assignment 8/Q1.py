#Calculate area of rectangle

def area_rectangle(length,width):
    return length * width

l = int(input("Enter  a length of rectangle"))
w = int(input("Enter a width of rectangle"))

area = area_rectangle(l,w)
print("Area of rectangle is:",area)