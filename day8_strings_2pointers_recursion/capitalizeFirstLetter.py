def capitalizeFirstLetter(s):
    if not s:
        return s
    return s[0].upper() + s[1:]
input_string = "hello world"
capitalized_string = capitalizeFirstLetter(input_string)
print(capitalized_string)