def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    result = []
    for index, item in enumerate(nums):
        count = 0
        for i in nums[:index] + nums[index+1:]:
            if i < item:
                count += 1
        result.append(count)

    return result
    
print(smallerNumbersThanCurrent([8,1,2,2,3]))