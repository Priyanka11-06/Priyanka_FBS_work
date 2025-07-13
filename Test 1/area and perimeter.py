# find area and perimeter

length= int(input("Enter a length of rectangle"))
breadth= int(input("Enter a breadth of rectangle"))
radius= int(input("Enter a radius of rectangle"))

rectangle_area = length * breadth
semicircle_area = 0.5 * 3.14 * radius ** 2
total_area = rectangle_area + semicircle_area

perimeter= length + (2 * breadth) + (3.14 * radius)

print("Area of figure:", total_area)
print("The perimeter is=", perimeter)
