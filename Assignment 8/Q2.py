# calculate area of circle

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area 

radius = float(input("Enter a radius :"))
result = area_of_circle(radius)
print("Area 0f circle is :",result)