# Convert feet and inches into meter into centimeters

feet = int(input("Enter discount in feet"))
inches = int(input("Enter remaining distance in inches"))

#foot = 0.3048 meters
#inches = 0.0254 meters

# Total marks
total_meters = (feet * 0.3048) + (inches * 0.0254)

meter = int(total_meters)
centimeter = (total_meters - meter) * 100

print("meters is =", meter)
print("centimeter is =", centimeter)