a1 = int(input("Enter a age of 1st people"))
a2 = int(input("Enter a age of 2nd people"))
a3 = int(input("Enter a age of 3rd people"))
a4 = int(input("Enter a age of 4th people"))
a5 = int(input("Enter a age of 5th people"))
amount = 100

if(a1<12):
    fair1 = amount - (amount * 0.3)
elif(a1>59):
    fair1 = amount * 0.5
else:
    fair1 = amount

if(a2<12):
    fair2 = amount - (amount * 0.3)
elif(a2>59):
    fair2 = amount * 0.5
else:
    fair2 = amount

if(a3<12):
    fair3 = amount - (amount * 0.3)
elif(a3>59):
    fair3 = amount * 0.5
else:
    fair3 = amount

if(a4<12):
    fair4 = amount - (amount * 0.3)
elif(a4>59):
    fair4 = amount * 0.5
else:
    fair4 = amount

if(a5<12):
    fair5 = amount - (amount * 0.3)
elif(a5>59):
    fair5 = amount * 0.5
else:
    fair5 = amount 

total = fair1+fair2+fair3+fair4+fair5
print("The total is " , total)

