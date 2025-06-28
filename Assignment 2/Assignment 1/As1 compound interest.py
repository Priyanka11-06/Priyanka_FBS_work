# To calculate compound interest

P= int(input("enter a principle"))
T= int(input("enter a time"))
R= int(input("enter a rate"))

CI= P*((1+R/100)**T)
print(" a compound interest=",CI)