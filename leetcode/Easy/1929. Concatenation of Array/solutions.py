def getConcatenation(nums: list[int]) -> list[int]:
    output = []
    for i in range(len(nums)*2):
        output.append(nums[i%len(nums)])
    
    return output

nums = [1,2,1]
output = getConcatenation(nums)
print(output)