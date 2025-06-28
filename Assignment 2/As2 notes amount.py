# program to find minimum no. of notes for given amount
amount = int(input("Enter amount"))

#500
n500 = amount // 500
r_amount = amount % 500

#200
n200 = amount // 200
r_amount = amount % 200

#100 
n100 = amount // 100
r_amount = amount % 100

#50
n50 = amount // 50
r_amount = amount % 50

#20
n20 = amount // 20
r_amount = amount % 20

#10 
n10 = amount // 10
r_amount = amount % 10

print(" Notes to be paid for amount" ,amount)
print ("Notes for 500 is=", n500)
print ("notes for 200", n200)
print ("notes for 100", n100)
print ("notes for 50", n50)
print ("notes for 20", n20)
print ("notes for 10", n10)