a = int(input("Enter value of a"))
i = 1
sum = 0

while i <= 10:
    sum += (a * i) / i
    i += 1

print("Sum of series", sum)