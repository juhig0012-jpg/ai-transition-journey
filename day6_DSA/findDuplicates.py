nums = [1, 2, 3, 2, 4, 5, 4
        , 6, 7, 8, 9, 10, 10]
duplicates = set()
for num in nums:
    if nums.count(num) > 1:
        duplicates.add(num)
print("Duplicate numbers in the list are:", duplicates)