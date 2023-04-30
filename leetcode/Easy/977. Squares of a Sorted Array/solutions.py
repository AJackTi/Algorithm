def sortedSquares(nums: list[int]) -> list[int]:
    return sorted(i * i for i in nums)

nums = [-4,-1,0,3,10]
print(sortedSquares(nums=nums))