def is_anagram(s, t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(is_anagram("listen", "silent"))
print(is_anagram("rat", "car"))