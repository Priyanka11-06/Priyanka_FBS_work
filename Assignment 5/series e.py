x = int(input("Enter a value of x"))
n = int(input("Enter number of terms"))
i = 1
term = 1
sum = 0
sign = 1
denominator = 1

while term <= n:
    sum += sign * (x ** term) / denominator
    term += 1
    denominator += 2
    sign += -1

print("Sum of series", sum)