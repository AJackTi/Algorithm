def arithmeticTriplets(nums: list[int], diff: int) -> int:
    count = 0
    setNums = set()
    
    for i in nums:
        if (i - 2 * diff) in setNums and (i - diff) in setNums:
            count += 1
        
        setNums.add(i)
         
    return count

nums = [0,1,4,6,7,10]
diff = 3
print(arithmeticTriplets(nums, diff))