list1 = [1, 2, 3, 4, 5, 2, 3]
# Removing duplicates using set
unique_list = list(set(list1))
if len(unique_list) < len(list1):
    print("Duplicates found.")
else:
    print("No duplicates found.")