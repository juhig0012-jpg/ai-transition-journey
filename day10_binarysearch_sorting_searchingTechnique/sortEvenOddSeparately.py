#sort even odd numbers separately
def sort_even_odd(nums):
    even_nums = []
    odd_nums = []

    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)

    even_nums.sort()
    odd_nums.sort()

    return even_nums + odd_nums
nums = [5, 2, 8, 1, 4]
result = sort_even_odd(nums)
print(result)