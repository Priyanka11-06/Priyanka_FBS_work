# To check given no is armstrong or not

def count(num):
    if(num!=0):
        return 1 + count(num//10)
    else:
        return 0
    
def armstrong(num,c):
    if(num!=0):
        digit = num % 10
        return digit ** c + armstrong(num//10,c)
    else:
        return 0
    
num = int(input("Enter a number"))
c = count(num)
ans = armstrong(num,c)

if(ans == num):
    print("Armstrong number")
else:
    print("Not armstromg")