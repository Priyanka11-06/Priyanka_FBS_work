# to check number is prime or not

def prime(num, i=2):
    if(num <= 1):
        return False
    if(2 * i > num):
        return True
    if(num % i == 0):
        return False
    return prime(num,i+1)

num = int(input("Enter a number"))
if prime(num):
    print("is a prime number")
else:
    print("is not a prime number")