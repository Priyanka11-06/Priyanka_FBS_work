cp = float(input("Enter a cost price"))
sp = float(input("Enter a selling price"))

if(sp > cp):
    profit = (sp-cp)
    print("profit", profit)
elif(cp > sp):
     loss = (cp-sp)
     print("loss", loss)
else:
     print("There is no profit or loss")
     
