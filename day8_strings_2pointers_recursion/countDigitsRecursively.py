def countDigitsRecursively(n):
    if n == 0:
        return 0
    else:
        return 1 + countDigitsRecursively(n // 10)
number = 12345
result = countDigitsRecursively(number)
print(f"The number of digits in {number} is: {result}")