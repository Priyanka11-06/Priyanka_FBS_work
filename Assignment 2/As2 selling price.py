# To calculate selling price of book based on cost price and discount

cost_price = float(input("Enter the cost price of the book"))
discount = float(input("Enter the discount percentage"))

discount_amount = (cost_price * discount) / 100
selling_price = cost_price - discount_amount 

print(" The selling price of the book is =", selling_price)