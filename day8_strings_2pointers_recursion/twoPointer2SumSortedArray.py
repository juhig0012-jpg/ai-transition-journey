def two_sum(nums, target):

    left = 0
    right = len(nums) - 1

    while left < right:

        current = nums[left] + nums[right]

        if current == target:
            return [left, right]

        elif current < target:
            left += 1

        else:
            right -= 1
    return []

nums = [1, 2, 3, 4, 5]
target = 7
result = two_sum(nums, target)
print(result)