def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1  # search right side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


arr = [1, 2, 2, 2, 3, 4]
print(last_occurrence(arr, 2))  # 3