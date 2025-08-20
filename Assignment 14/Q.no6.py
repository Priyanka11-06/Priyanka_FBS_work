num = [1,10,3,9,2,6]
max_product = float('-inf')
pair = ()

for i in range(len(num)):
    for j in range(i+1, len(num)):
        product = num[i] * num[j]
        if(product > max_product):
            max_product = product
            pair = (num[i], num[j])

print("Two numbers:", pair, "with  max product:", max_product)