# remove all occurance of given element

list1 = [34,65,87,43,90,40,65,43]
ele = int(input("Enter the element"))
c = 0
for i in range(len(list1)):
    if(ele == list1[i]):
        c += 1
for i in range(c):
    list1.remove(ele)
print(list1)
