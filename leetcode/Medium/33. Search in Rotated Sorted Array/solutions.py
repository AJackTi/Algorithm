def search(nums: list[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    
    return -1