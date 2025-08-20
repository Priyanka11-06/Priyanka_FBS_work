# create new list from existing list which contain cube of each element

list1 = [5,6,3,5,7,]
list2 = []
for i in list1:
    cube = i*i*i
    list2.append(cube)
print(list1)
print(list2)