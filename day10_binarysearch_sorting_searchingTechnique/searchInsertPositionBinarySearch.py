def search_insert_position(nums, target):

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return left


nums = [1, 3, 5, 6]

print(search_insert_position(nums, 5))  # 2
print(search_insert_position(nums, 2))  # 1
print(search_insert_position(nums, 7))  # 4