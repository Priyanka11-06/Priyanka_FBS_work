#      1 
#     1 1 
#    1 2 1 
#   1 3 3 1 


row = 4
for i in range(row):
   print(" " * (row-i),end=" ")
   x = 1
   for j in range(i+1):
      print(x,end=" ")
      x = x * (i-j)//(j+1)
   print()


   