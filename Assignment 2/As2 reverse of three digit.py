# Write a program to reverse three digit number

num = int(input("Enter a three digit no."))
a = num % 10
num = num //10
b = num % 10
reverse = (a*10) + b
c = num // 10
reverse = (reverse * 10) + c

print("The reverse of three digit number is", reverse)