def findDuplicateCharacters(s):
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    duplicates = {char: count for char, count in frequency.items() if count > 1}
    return duplicates
input_string = "programming"
duplicates = findDuplicateCharacters(input_string)
print(duplicates)