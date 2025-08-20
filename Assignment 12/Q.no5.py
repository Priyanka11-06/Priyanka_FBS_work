str = input("Enter a string:")
vowels = "aeiou"
count = 0
for i in str:
    for j in vowels:
        if i == j:
            count += 1
print("Number of vowels ", count)