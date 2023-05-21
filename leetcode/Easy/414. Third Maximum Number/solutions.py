def thirdMax(nums: list[int]) -> int:
    ans = [-2**31,-2**31,-2**31]
    idx = 0
    for i in range(len(nums)):
        while(idx < len(ans)):
            if nums[i] < -2**31 or nums[i] > 2**31-1:
                continue
            if nums[i] == ans[idx]:
                break
            elif nums[i] > ans[idx] and ans.count(nums[i]) == 0:
                ans.insert(idx, nums[i])
                break
            else:
                idx+=1
        if idx == len(ans):
            ans[2] = nums[i]
        idx = 0
    
    return ans[2] if len(set(nums)) >= 3 else ans[0]

# nums = [2,2,3,1]
# nums = [3,2,1]
# nums = [1,2]
# nums = [-2147483648,1,1]
nums = [1,2,2,5,3,5]
print(thirdMax(nums=nums))