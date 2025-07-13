num = int(input("Enter a number"))
copy = num

a = num%10
num = num // 10
b = num % 10
reverse = (a * 10) + b
c = num // 10 
reverse = (reverse * 10) + c

if(copy == reverse):
    print("The number is palindrome")
else:
    print("The number is not palindrome")