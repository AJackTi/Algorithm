def numToList(num: int) -> list[int]:
    arr = []
    while num > 0:
        arr.append(num % 10)
        num //=10
        
    return arr[::-1]

def separateDigits(nums: list[int]) -> list[int]:
    result = []
    for i in nums:
        result += numToList(i)
    return result

nums = [13,25,83,77]
print(separateDigits(nums=nums))