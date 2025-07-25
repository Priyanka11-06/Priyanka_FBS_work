# to find sum of digit

def sOD(num):
    if(num==0):
        return 0
    else:
        a = num % 10
        return a+sOD(num//10)
    
num = int(input("Enter a number"))
print(sOD(num))