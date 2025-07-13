correct_userid = "piyuu"
correct_password = "2105"
attempt = 0

while attempt < 3:
    userid = input("Enter your id")
    password = input("Enter password")

    if(userid == correct_userid and password == correct_password):
        print("Login successful")
        break
    else:
        print("Incorrect userid and password")

if(attempt == 3):
    print("wrong credentials. program terminated")
