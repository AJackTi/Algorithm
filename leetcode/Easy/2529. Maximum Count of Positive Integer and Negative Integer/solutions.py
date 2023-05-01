def maximumCount(nums: list[int]) -> int:
    max_negative = 0
    max_positive = 0
    for i in nums:
        if i > 0:
            max_positive += 1
        if i < 0:
            max_negative += 1
            
    return max(max_positive, max_negative)