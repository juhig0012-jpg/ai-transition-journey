#sort dictionay by values
my_dict = {
    "apple": 3,
    "banana": 1,
    "cherry": 2
}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)