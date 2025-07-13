passenger = int(input("Enter a number of passenger"))
ticket_cost = float(input("Ente cost of one ticket"))

count = 0
total_amt = 0

while count < passenger:
    age = int(input("Enter age of passenger"))

    if(age < 12):
        cost = ticket_cost * 0.7
    elif(age > 59):
        cost = ticket_cost * 0.5
    else:
        cost = ticket_cost
    total_amt += cost
    count += 1

    
    

print("total amount to br paid for all passenger",total_amt)