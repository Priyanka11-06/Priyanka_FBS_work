def count_digit(num):
    count = 0
    while(num>0):
        num = num//10
        count += 1
    return count

def armstrong_sum(num,digits):
    temp = num
    result = 0
    while(temp>0):
        digit = temp % 10
        result += digit ** digits
        temp = temp // 10
    return result

def is_armstrong(num):
    digit = count_digit(num)
    return num == armstrong_sum(num,digit)
n = int(input("Enter a number"))
if(is_armstrong(n)):
    print(n,"is armstrong number")
else:
    print(n," is not armstrong number")