# find max and min number 
list1=[]
num=int(input("enter a no:"))
for i in range(num):  #range(1,n+1)
    marks=int(input("enter a marks:"))
    list1.append(marks)
print("the marks of std",list1)
min_marks=min(list1)
max_marks=max(list1)
print(f'min:{min_marks},max:{max_marks}')