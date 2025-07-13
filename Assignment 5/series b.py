n = int(input("Enter n"))
i = 1
sum = 0

while i <= n:
    sum += n ** i
    i += 1

print("Sum of powers", sum)