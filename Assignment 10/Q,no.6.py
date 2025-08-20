# remove duplicates from the list

list1 = [50,76,56,50,40,37,40,32]
list2 = []
for i in list1:
    if(i not in list2):
        list2.append(i)

print(list1)
print("Afte removing duplicates",list2)
 
