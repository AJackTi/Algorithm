def leftRigthDifference(nums: list[int]) -> list[int]:
    left = [0] * len(nums)
    right = [0] * len(nums)
    for i in range(1, len(nums)):
        left[i] = sum(nums[:i])
        right[i-1] = sum(nums[i:])
    
    result = list()
    for item1, item2 in zip(left, right):
        item = item1 - item2 if item1 > item2 else item2 - item1
        result.append(item)
    
    return result

print(leftRigthDifference([10, 4, 8, 3]))