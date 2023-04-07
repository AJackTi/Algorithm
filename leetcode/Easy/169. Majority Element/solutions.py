import operator

def majorityElement(nums: list[int]) -> int:
    dict = {}
    for i in nums:
        if i not in dict:
            dict[i] = 1
            continue
        dict[i] += 1
    
    return max(dict.items(), key=operator.itemgetter(1))[0]

print(majorityElement([2,2,1,1,1,2,2]))