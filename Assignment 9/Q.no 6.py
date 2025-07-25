# To print fibonancci series

def fibbo(a,b,num):
    if(num>0):
        c = a+b
        print(c)
        fibbo(b,c,num-1)

num = int(input("Enter a number"))
fibbo(-1,1,num)