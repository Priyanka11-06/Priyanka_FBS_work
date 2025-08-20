str = input("Enter a string :")
if(len(str)< 2):
    print("String is not to start to swap:")
else:
    new_str = str[-1] + str[1:-1] + str[0]
print("New string ", new_str)