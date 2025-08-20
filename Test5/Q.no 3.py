Data =[[101, "Seema", 45000], [340, "Rajan", 13000], [210, "Tanuu", 14000], [320, "Suresh", 35000]]

sort_Data = sorted(Data, key = lambda x:x[2])
print("Sorted by salary")
for emp in sort_Data:
    print(emp)
