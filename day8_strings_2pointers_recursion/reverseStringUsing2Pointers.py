def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
input_string = list("Hello, World!")
reversed_string = reverse_string(input_string)
print(''.join(reversed_string))