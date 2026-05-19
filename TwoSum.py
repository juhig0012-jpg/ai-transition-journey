def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        remaining = target - num

        if remaining in seen:
            return [seen[remaining], i]

        seen[num] = i


# Example 1
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))   # Output: [0, 1]

# Example 2
nums = [3, 2, 4]
target = 6
print(two_sum(nums, target))   # Output: [1, 2]

# Example 3
nums = [3, 3]
target = 6
print(two_sum(nums, target))   # Output: [0, 1]