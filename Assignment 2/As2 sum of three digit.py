# sum of digit of three digit no.

num = int(input("Enter three digit no"))

a = num % 10
num = num // 10
c = num % 10
d = num // 10
sum = a+c+d

print("The sum of three digit no. is =",sum)