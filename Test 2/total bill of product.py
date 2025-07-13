p1 = int(input("Enter a price of product 1:"))
p2 = int(input("Enter a price of product 2:"))
p3 = int(input("Enter a price of product 3:"))
p4 = int(input("Enter a price of product 4:"))
p5 = int(input("Enter a price of product 5:"))

if(p1>0 and p2>0 and p3>0 and p4>0 and p5>0):
    total = p1+p2+p3+p4+p5
    gst = total*0.18
    total_bill = total+gst
    print("Total bill after gst is rs", total_bill)
else:
    print("All product priced must be greater than 0")