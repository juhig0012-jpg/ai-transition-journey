#find kth largest element in an array
def find_kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k - 1]      
nums = [3, 1, 5, 2, 4]
k = 2
result = find_kth_largest(nums, k)
print(result)