# find even or odd element  and  create a seperate teo list

num = int(input("Enter the no of elements"))
list1 = []
for i in range(num):
    ele = int(input("Enter a element"))
    list1 = list1 + [ele]
even_list2 = []
odd_list3 = []
for i in range(len(list1)):
    if(list1[i]%2==0):
        even_list2 = even_list2 + [list1[i]]
    else:
        odd_list3 = odd_list3 + [list1[i]]
print(list1)
print(even_list2)
print(odd_list3)