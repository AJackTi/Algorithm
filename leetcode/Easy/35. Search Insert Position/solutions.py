def searchInsert(nums: list[int], target: int) -> int:
    if nums.count(target) != 0:
        return nums.index(target)
    if target > nums[len(nums) - 1]:
        return len(nums)

    for index, value in enumerate(nums):
        if value > target:
            return index
        
print(searchInsert([1,3,5,6], 7))