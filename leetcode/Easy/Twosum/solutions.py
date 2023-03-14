def twoSum(nums, target):
    dic = dict()
    for index, num in enumerate(nums):
        x = target - num
        if x in dic:
            return dic[x], index
        dic[num] = index