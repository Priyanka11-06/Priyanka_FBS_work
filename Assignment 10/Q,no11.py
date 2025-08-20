# print element which are divisibe by m and n

num = int(input("Enter the no of element"))
list1 = []
for i in range (num):
     ele = int(input("Enter the element"))
     list1.append(ele)
print("list given by user",list1)

m = int(input("Enter a first divisior:"))
n = int(input("Enter a second divisior"))
new_list = []
for i in range(num):
     if(list1[i]%m==0 and list1[i]%n==0):
          new_list.append(list1[i])
print(new_list)