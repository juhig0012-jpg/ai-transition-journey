def max_sum(nums, k):

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):

        window_sum += nums[i]
        window_sum -= nums[i-k]

        max_sum = max(max_sum, window_sum)

    return max_sum
nums = [1, 2, 3, 4, 5]
k = 2
result = max_sum(nums, k)
print("Maximum sum of a subarray of size", k, "is:", result)