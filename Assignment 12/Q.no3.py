str1 = input("Enter first string")
str2 = input("Enter second string")

str1 = str1.replace(" "," ")
str2 = str2.replace(" "," ")

if sorted(str1)==sorted(str2):
    print("The string are anagram")

else:
    print("The string are not anagram")