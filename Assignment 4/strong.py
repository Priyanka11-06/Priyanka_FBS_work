sum = 0
num = int(input("Enter a number"))
temp = num

while(temp !=0):
    a = temp%10
    fact = 1
    
    for i in range(1,a+1):
        fact*=i
    sum += fact
    temp = temp//10
if(sum==num):
    print("It is a strong number")
else:
    print("It is not a strong number")