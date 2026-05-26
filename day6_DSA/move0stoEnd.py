nums = [7, 0, 5, 0, 3, 0, 1]
non_zero_nums = [num for num in nums if num != 0]
zero_count = nums.count(0)
result = non_zero_nums + [0] * zero_count
print("List after moving zeros to the end:", result)