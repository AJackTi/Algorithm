def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    first = set(nums1)
    second = set(nums2)
    return [list(first.difference(second)), list(second.difference(first))]

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1=nums1, nums2=nums2))