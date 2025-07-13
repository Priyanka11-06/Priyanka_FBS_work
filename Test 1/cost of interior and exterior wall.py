# find area and cost of both interior and exterior wall

interior_area = float(input("Enter interior wall area"))
interior_cost = float(input("Enter cost for interior painting"))

exterior_area = float(input("Enter exterior wall area"))
exterior_cost = float(input("Enter cost for exterior painting")) 

interior_total_cost = interior_area * interior_cost
exterior_total_cost = exterior_area * exterior_cost
total_cost = interior_total_cost + exterior_total_cost

print("cost of painting interior walls is:", interior_total_cost)
print("cost of painting exterior walls is:", exterior_total_cost)
print("Total painting cost:", total_cost)








