x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evennumbers = filter(lambda num: num % 2 == 0, x)
squared_even_numbers = map(lambda num: num ** 2, evennumbers)
print(list(squared_even_numbers))