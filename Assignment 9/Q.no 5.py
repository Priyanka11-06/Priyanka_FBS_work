# To finf factorial

def factorial(num):
    if(num==1):
        return 1
    else:
        return num*factorial(num-1)
    
num = int(input("Enter a number"))
x = factorial(num)
print(x)