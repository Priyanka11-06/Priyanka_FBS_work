n = int(input("Enter number of terms"))
i = 0
sum = 0
term = 1

while i < n:
    sum += term
    term *= 2
    i += 1

print("sum of geometric series", sum)