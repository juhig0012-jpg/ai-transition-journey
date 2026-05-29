# Text Analyzer Program

from collections import Counter

# Input sentence
text = input("Enter a sentence: ")

# Word Count
word_count = len(text.split())

# Vowel Count
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)

# Palindrome Check
clean_text = ''.join(char.lower() for char in text if char.isalnum())
is_palindrome = clean_text == clean_text[::-1]

# Character Frequency
char_frequency = Counter(text)

# Reversed Sentence
reversed_text = text[::-1]

# Output
print("\n--- Text Analyzer Result ---")
print(f"Word Count: {word_count}")
print(f"Vowel Count: {vowel_count}")
print(f"Palindrome Check: {'Yes' if is_palindrome else 'No'}")
print(f"Reversed Sentence: {reversed_text}")

print("\nCharacter Frequency:")
for char, freq in char_frequency.items():
    print(f"'{char}': {freq}")