def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumOfDigits(n // 10)
number = 12345
result = sumOfDigits(number)
print(f"The sum of digits in {number} is: {result}")