def buildArray(nums: list[int]) -> list[int]:
    result = []
    for i in nums:
        result.append(nums[i])

    return result

nums = [0,2,1,5,3,4]
output = buildArray(nums)
print(output)