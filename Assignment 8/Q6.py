def fibonancci(num):
    a = 1
    b = 0
    print(a,b,end=" ")
    for i in range(2,num):
        c = a+b
        print(c,end=" ")
        a = b
        b = c
num = int(input("Enter a number :"))
if(num<=0):
    print("plz enter a positive integer")
elif(num==1):
    print(i)
else:
    print("fibonancci series",fibonancci(num))

