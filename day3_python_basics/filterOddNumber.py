x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter(lambda num: num % 2 != 0, x)
print(list(odd_numbers))