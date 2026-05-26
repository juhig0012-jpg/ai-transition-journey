a = 'hi there'
hashmap = {}
for char in a:
    hashmap[char] = hashmap.get(char, 0) + 1    
first_non_repeating_char = None
for char in a:
    if hashmap[char] == 1:
        first_non_repeating_char = char
        break

print("First non-repeating character:", first_non_repeating_char)