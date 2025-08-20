str = input("Enter a string")
digit = letter = 0
for i in str:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        letter += 1
    
print("number of letter:",letter)
print("number of digit:",digit)