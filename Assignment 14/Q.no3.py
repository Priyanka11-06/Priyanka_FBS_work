words = ["apple", "banana","apple", "orange", "banana", "apple"]
unique_words = set(words)

for word in unique_words:
    print(word,":", words.count(word))