start = int(input("Enter a start range"))
stop = int(input("Enter a stop range"))
divisible = int(input("Enter the divisible number"))

print("The number in a range divisible by give number are: ")
for i in range(start,stop+1):
     if(i%divisible==0):
          print(i)