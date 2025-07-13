a1 = int(input("Enter a 1st angle"))
a2 = int(input("Enter a 2nd angle"))
a3 = int(input("Enter a 3rd angle"))

if(a1+a2+a3 == 180 and a1>0 and a2>0 and a3>0):
    print("Triangle is valid")
else:
    print("Triangle in invalid")