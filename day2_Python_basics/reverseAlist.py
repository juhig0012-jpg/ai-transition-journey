lst = [1, 2, 3, 4, 5]
reversed_list = []

for item in lst:
    reversed_list = [item] + reversed_list

print(reversed_list)