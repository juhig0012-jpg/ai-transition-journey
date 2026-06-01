def reverseStringUsingStack(s):
    stack = []
    for char in s:
        stack.append(char)
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()
    return reversed_string
input_string = "Hello, World!"
reversed_string = reverseStringUsingStack(input_string)
print(reversed_string)