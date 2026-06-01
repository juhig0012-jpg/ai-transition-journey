def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)

    if first == -1:
        return 0

    last = last_occurrence(arr, target)

    return last - first + 1


arr = [1, 2, 2, 2, 3, 4]
print(count_occurrences(arr, 2))  # 3