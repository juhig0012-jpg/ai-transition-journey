def reverseStringRecursively(s):
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverseStringRecursively(s[:-1])
input_string = "Hello, World!"
reversed_string = reverseStringRecursively(input_string)
print(reversed_string)