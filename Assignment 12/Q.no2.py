# Remove the nth index character from non empty string

str = input("Enter the string")
num = int(input("Enter the index of character to remove"))
result = ""
x = 0
for i in str:
    if x != num:
        result += i
    x += 1
print("updated string", result)
