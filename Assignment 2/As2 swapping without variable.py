# write a program to swap two numbers without using third variable

num1 = int(input("Enter a first number"))
num2 =  int(input("Enter a second number"))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print("After swapping num1 is=", num1, "num2 =", num2)