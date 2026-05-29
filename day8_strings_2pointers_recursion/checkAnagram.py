def check_Anagram(s1, s2):
    # Remove spaces and convert to lowercase
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    
    # Sort the characters of both strings
    return sorted(s1) == sorted(s2)
    
string1 = "listen"
string2 = "silent"
if check_Anagram(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")