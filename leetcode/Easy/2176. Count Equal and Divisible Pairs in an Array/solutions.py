def countPairs(nums: list[int], k: int) -> int:
    if len(set(nums)) == len(nums):
        return 0
    
    count = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i * j % k == 0:
                count += 1
                
    return count

nums = [3,1,2,2,2,1,3]
k = 2
print(countPairs(nums=nums, k=k))