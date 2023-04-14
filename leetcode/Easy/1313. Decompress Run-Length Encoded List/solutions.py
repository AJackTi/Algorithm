def decompressRLElist(nums: list[int]) -> list[int]:
    result = []
    for i in range(0, len(nums), 2):
        result += nums[i] * [nums[i+1]]
    
    return result

nums = [1,1,2,3]
print(decompressRLElist(nums))