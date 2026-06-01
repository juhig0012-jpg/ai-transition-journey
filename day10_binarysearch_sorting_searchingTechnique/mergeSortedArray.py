def merge(nums1, nums2):

    result = []

    i = 0
    j = 0

    while i < len(nums1) and j < len(nums2):

        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1

        else:
            result.append(nums2[j])
            j += 1

    result.extend(nums1[i:])
    result.extend(nums2[j:])

    return result
nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
result = merge(nums1, nums2)
print(result)