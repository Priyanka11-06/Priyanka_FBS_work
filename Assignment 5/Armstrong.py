num = int(input("Enter a number to check if it is a armstrong number"))
temp = num
order = len(str(num))
sum_armstrong = 0

while temp > 0:
    digit = temp % 10
    sum_armstrong += digit ** order
    temp//=10

if(sum_armstrong == num):
    print("It is armstrong number", num)
else:
    print("It is not a armstrong number", num)