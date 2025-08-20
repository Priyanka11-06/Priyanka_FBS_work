# reverse the list

list1 = [10,20,30,40,50]
rev_list2 = []

for i in range(len(list1)-1,-1,-1):
    rev_list2.append(list1[i])

print(list1)
print(rev_list2)