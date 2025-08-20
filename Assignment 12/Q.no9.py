str = input("Enter a string")
words = str.split()
num_words = len(words)
count_char = 0
for i in str:
    if(i != " "):
        count_char += 1
print("Number of words ", num_words)
print("anumber of character:", count_char)