def containsDuplicate(nums: list[int]) -> bool:
    hset = set()
    for idx in nums:
        if idx in hset:
            return True
        else:
            hset.add(idx)