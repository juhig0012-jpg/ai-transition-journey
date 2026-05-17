first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
third = int(input("Enter third number: "))
if first >= second and first >= third:
    print("Largest number is:", first)
elif second >= first and second >= third:
    print("Largest number is:", second)
else:
    print("Largest number is:", third)