def is_palindrome(s):

    cleaned = ""

    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()

    return cleaned == cleaned[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))