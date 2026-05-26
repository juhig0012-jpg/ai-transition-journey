a = 'hi there'
char_count = {}
hashmap = {}
for char in a:
    hashmap[char] = hashmap.get(char, 0) + 1
print(hashmap)
