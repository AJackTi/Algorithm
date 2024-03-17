def maxProduct(nums: list[int]) -> int:
    res = max(nums)
    cur_max, cur_min = 1, 1

    for n in nums:
        tmp = cur_max * n
        cur_max = max(n * cur_max, n * cur_min, n)
        cur_min = min(tmp, n * cur_min, n)
        res = max(res, cur_max)

    return res


print(maxProduct([2, 3, -2, 4]))
