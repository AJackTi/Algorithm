def runningSum(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        result.append(sum(nums[:i+1]))
    
    return result