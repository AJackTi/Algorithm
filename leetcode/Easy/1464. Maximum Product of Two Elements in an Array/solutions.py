def maxProduct(nums: list[int]) -> int:
    nums.sort(reverse=True)
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return (nums[0]-1)*(nums[0]-1)
    return (nums[0]-1)*(nums[1]-1)

print(maxProduct([3,4,5,2]))