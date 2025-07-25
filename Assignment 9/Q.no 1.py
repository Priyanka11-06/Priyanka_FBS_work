# 1! + 2! + 3! +...........n
# for fact

def fact(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * fact(num-1)
    
# sum of fact

def sum(num):
    if(num == 1):
        return fact(1)
    else:
        return fact(num) + sum(num-1)
    
num = int(input("Enter a number"))
result = sum(num)
print("sum os series 1! + 2! + 3! +..........n is :",result)