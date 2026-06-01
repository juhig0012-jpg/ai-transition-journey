def first_occurrence(nums, target):

    left = 0
    right = len(nums) - 1

    result = -1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            result = mid
            right = mid - 1

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return result
nums = [1, 2, 2, 3, 4]
target = 2
result = first_occurrence(nums, target)
print(result)