# To convert days into year, weeks and days

days=int(input("enter a days"))

years= days//365
days= days%365
weeks= days//7
days= days%7

print("years=",years)
print("weeks=",weeks)
print("days=",days)