def sumDigit(no):
    return 0 if no == 0 else int(no % 10) + sumDigit(no // 10)

def differenceOfSum(nums: list[int]) -> int:
    sumNums = sum(nums)
    sumDigits = 0
    for i in nums:
        sumDigits += sumDigit(i)
    
    return abs(sumNums - sumDigits)

nums = [1,15,6,3]
print(differenceOfSum(nums))