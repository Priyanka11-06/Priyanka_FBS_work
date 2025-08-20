# duplicate of existing list ,not print to same list

list1 = [10,20,30,40,50]
list2 = []

for i in list1:
    list2 += [i]
print("original list",list1)
print("Dulicate list",list2)
