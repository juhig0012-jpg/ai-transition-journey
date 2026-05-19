text = "hello world"
freq = {}

for ch in text:
    if ch != " ":  # ignoring spaces
        freq[ch] = freq.get(ch, 0) + 1

print(freq)