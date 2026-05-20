square = lambda x: x ** 2
number = int(input("Enter a number: "))
result = square(number)
print(f"The square of {number} is: {result}")
mylist = [1, 2, 3, 4, 5]
squared_list = list(map(lambda x: x ** 2, mylist))
print(f"The squared list is: {squared_list}")
