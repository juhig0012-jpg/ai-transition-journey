nums = [1,7,9,2,3,4]
min_num = nums[0]
for i in range(1, len(nums)):
    if nums[i] < min_num:
        min_num = nums[i]
print("Minimum number in the list is:", min_num)