from functools import reduce
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_of_list = reduce(lambda a, b: a + b, x)
print(sum_of_list)