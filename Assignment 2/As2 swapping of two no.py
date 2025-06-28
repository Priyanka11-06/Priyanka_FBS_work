# Write a program to swap two numbers using third variable

num1 = int(input("Enter a first number"))
num2 = int(input("Enter a second number"))

temp = num1
num1 = num2
num2 = temp

print("After swapping num1 is =",num1, "num2 =", num2)
