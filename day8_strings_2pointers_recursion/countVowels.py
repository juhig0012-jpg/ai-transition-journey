text = 'I love AI'
def count_vowels(s, i=0):
    frequency = {}
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            frequency[char] = frequency.get(char, 0) + 1
    return frequency
count =count_vowels(text)
print(count)