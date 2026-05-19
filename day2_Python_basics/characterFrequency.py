def char_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

s = input("Enter a string: ")
print(char_frequency(s))