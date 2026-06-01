def square_root(n):

    if n < 2:
        return n

    left, right = 1, n
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid

        elif mid * mid < n:
            ans = mid
            left = mid + 1

        else:
            right = mid - 1

    return ans


print(square_root(25))  # 5
print(square_root(20))  # 4