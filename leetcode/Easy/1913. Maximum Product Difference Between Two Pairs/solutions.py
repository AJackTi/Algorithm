def maxProductDifference(nums: list[int]) -> int:
    nums.sort()
    return nums[-1] * nums[-2] - nums[0] * nums[1]