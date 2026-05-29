def powerFunctionRecursive(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / powerFunctionRecursive(base, -exponent)
    else:
        return base * powerFunctionRecursive(base, exponent - 1)
base = 2
exponent = 3

result = powerFunctionRecursive(base, exponent)
print(f"{base} raised to the power of {exponent} is: {result}")