# To reverse a given number

def reverse(num,rev):
    if(num!=0):
        a = num % 10
        rev = rev * 10 + a
        return reverse(num//10,rev)
    else:
        return rev
    
num = int(input("Enter number"))
ans = reverse(num,0)
print("The reverse number is :",ans)