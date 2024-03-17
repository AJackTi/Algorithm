def maxProduct(nums: list[int]) -> int:
    res = max(nums)
    curMax, curMin = 1, 1

    for n in nums:
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(res, curMax)

    return res


print(maxProduct([2, 3, -2, 4]))
