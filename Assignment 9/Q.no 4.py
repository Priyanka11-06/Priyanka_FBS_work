# To find sum of n numbers

def sum(num):
    if(num == 0):
        return 0
    return num + sum(num-1)

num = int(input("Enter a number"))
print("sum is :",sum(num))