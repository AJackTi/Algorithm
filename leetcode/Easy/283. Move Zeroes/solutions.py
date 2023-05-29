def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == 0 and nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                break

nums = [0,1,0,3,12]
moveZeroes(nums=nums)
print(nums)