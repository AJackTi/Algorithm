def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums)
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid    
        elif target < nums[mid]:
            right = mid-1
        else:
            left = mid+1

    return -1
    
nums = [-1,0,3,5,9,12]
target = 9
# nums = [-1,0,3,5,9,12]
# target = 2
print(search(nums=nums, target=target))