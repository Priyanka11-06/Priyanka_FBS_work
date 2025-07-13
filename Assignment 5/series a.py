n = int(input("Enter n"))
i = 1
sum = 0

while i <= n:
    fact = 1
    j = 1

    while j <= i:
        fact *= j
        j += 1
    sum += fact
    i += 1

print("Sum of factorial series", sum)