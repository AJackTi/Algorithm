import operator

def singleNumber(nums: list[int]) -> int:
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 1
            continue
        dict[i] += 1
    
    return min(dict.items(), key=operator.itemgetter(1))[0]

print(singleNumber([4,1,2,1,2]))