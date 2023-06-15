from bisect import bisect_left, bisect_right


def searchRange(nums: list[int], target: int) -> list[int]:
    # n = len(nums)
    # def findFirstPos(nums, target):
    #     left = 0
    #     right = n - 1
    #     ans = -1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target:
    #             ans = mid
    #             right = mid - 1
    #         elif target > nums[mid]:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return ans
    
    # def findLastPos(nums, target):
    #     left = 0
    #     right = n - 1
    #     ans = -1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target:
    #             ans = mid
    #             left = mid + 1
    #         elif target > nums[mid]:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return ans
    
    # return [findFirstPos(nums, target), findLastPos(nums, target)]
    
    n = len(nums)
    iLeft = bisect_left(nums, target)
    if iLeft == n or nums[iLeft] != target:
        return [-1, -1]
    
    iRight = bisect_right(nums, target) - 1
    
    return [iLeft, iRight]
    

nums = [5,7,7,8,9,10]
target = 8
print(searchRange(nums=nums, target=target))