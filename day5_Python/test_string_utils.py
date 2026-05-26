# test_string_utils.py

from string_utils import reverse_string, count_vowels

sample_text = "Hello Python"

reversed_text = reverse_string(sample_text)
vowel_count = count_vowels(sample_text)

print("Original String:", sample_text)
print("Reversed String:", reversed_text)
print("Vowel Count:", vowel_count)