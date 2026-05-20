def factorialcheck(num):
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return "The factorial of 0 is 1"
    else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        return f"The factorial of {num} is {factorial}"
number = int(input("Enter a number: "))
result = factorialcheck(number) 
print(result)
