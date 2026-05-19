class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


input_array = list(map(int, input("Enter the array elements separated by space: ").split()))

solution = Solution()

print("Maximum subarray sum:", solution.maxSubArray(input_array))