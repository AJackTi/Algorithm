def removeElement(nums: list[int], val: int) -> int:
    while val in nums:
        nums.remove(val)