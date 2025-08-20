# Remove the characters of odd index values in a string

str = input("Enter a string")
result = ""
x = 0
for i in str:
    if x%2 == 0:
        result += i
    x += 1
print("Updated string ",result)