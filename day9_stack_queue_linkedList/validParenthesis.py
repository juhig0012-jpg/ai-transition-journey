def is_valid(s):

    stack = []

    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for ch in s:

        if ch in mapping.values():
            stack.append(ch)

        elif ch in mapping.keys():

            if not stack or stack.pop() != mapping[ch]:
                return False

    return len(stack) == 0

print(is_valid("()[]{}"))
print(is_valid("([)]"))
print(is_valid("{[]}"))