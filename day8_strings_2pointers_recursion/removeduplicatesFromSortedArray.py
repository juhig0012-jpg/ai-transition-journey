def removeDuplicates(nums):
    if not nums:
        return 0
    write_index = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    return write_index
nums = [1, 1, 2, 3, 3, 4]
new_length = removeDuplicates(nums)
print(new_length)
print(nums[:new_length])