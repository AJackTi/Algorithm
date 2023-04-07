def missingNumber(nums: list[int]) -> int:
    return int(len(nums)*(len(nums)+1)/2 - sum(nums))