# element is present or not and how many times is present

list1 = [10,20,30,40,50,40,30,40]
num = int(input("Enter a number"))
count = 0
for i in range(len(list1)):
    if(num==list1[i]):
        count += 1
if(count>0):
    print("yes,It is present")
    print("It occurs",count)
else:
    print("No,It is not present")