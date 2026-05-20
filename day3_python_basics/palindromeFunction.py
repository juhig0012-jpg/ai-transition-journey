def checkpalindrome(word):
    word = word.lower()
    return word == word[::-1]

word = input("Enter a word: ")
if checkpalindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")