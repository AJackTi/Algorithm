def findMaxConsecutiveOnes(nums: list[int]) -> int:
    maxConsecutiveOnes = 0
    consecutiveOnes = 0
    for i in nums:
        if i == 1:
            consecutiveOnes += 1
        else:
            consecutiveOnes = 0
        
        maxConsecutiveOnes = max(maxConsecutiveOnes, consecutiveOnes)
        
    return maxConsecutiveOnes

nums = [1,1,0,1,1,1]
# nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums=nums))