per = float(input("Enter a percentage"))

if(per>=80 and per<=100):
   print(" First class with above Distinction: ")
elif(per>=70 and per<80):
   print("first class")
elif(per>=60 and per<70):
   print("Higher second class") 
elif(per>=40 and per<60):
   print("Second class")
elif(per<40 and per>=0):
   print("Fail")

else:
   print("Wrong input")
   



