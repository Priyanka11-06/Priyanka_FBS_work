import random
userid = input("Enter userid")
pass1 = input("Enter pass")

if(userid == "FBS" and pass1 == "FBS123"):
    captcha = random.randint(1000,9999)
    print("captcha", captcha)
    input = int(input("Enter captcha"))
    if(input == captcha):
       print("successful login")
    else:
        print("captcha failed")
else:
    print("unsuccessful login")


