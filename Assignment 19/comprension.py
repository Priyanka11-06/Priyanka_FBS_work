# 1. Find all of the numbers from 1-1000 that are divisible by 8

num = [n for n in range(1,1000) if n % 8==0]
print(num)

# # 2. find all of the numbers from 1-1000 that have a 6 in them

num = [ n for n in range(1,1000) if '6' in str(n)]
print(num)

# 3. count the number of space in a string 

s = input("Enter a string")
space = s.count(" ")
print("Number of space", space) 

# 4. Remove all the vowels in a string

s = input("Enter a string")
vowels = "aeiouAEIOU"
result = " ".join([ch for ch in s if ch not in vowels])
print("String without vowels:",result)

# 5. Find all of the words in a string that are less tahn 5 letters

s = input("Enter a string:")
words = [word for word in s.split() if len(word) < 5]
print("Word with less than 5 letters:",words)

# 6. Use a dictionary comprehension to count the length of each word in a sentence

s = input("Enter a Sentence")
word_lengths = {word:len(word) for word in s.split()}
print("word length:",word_lengths)

# 7. Use a nested list comprehension to find all the numbers from the 1-1000 that are divisible by any single digit

num = [n for n in range(1,1001) if any(n % d==0 for d in range(2,10))]
print(num)

