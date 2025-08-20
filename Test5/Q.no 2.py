def missing_coin(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

coins = [5, 7, 2, 7, 5, 2, 5]
print("Missing coins", missing_coin(coins))