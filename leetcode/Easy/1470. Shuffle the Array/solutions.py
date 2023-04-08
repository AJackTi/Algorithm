def shuffle(nums: list[int], n: int) -> list[int]:
    result = []
    for i in range(0, n):
        result.append(nums[i])
        result.append(nums[n+i])
    
    return result
