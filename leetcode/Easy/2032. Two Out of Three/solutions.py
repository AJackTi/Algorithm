def twoOutOfThree(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    lst_ans = []
    set_total = set(nums1 + nums2 + nums3)
    for i in set_total:
        if list(set(nums1)).count(i) + list(set(nums2)).count(i) + list(set(nums3)).count(i) > 1:
            lst_ans.append(i)
            
    return lst_ans

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]
print(twoOutOfThree(nums1=nums1, nums2=nums2, nums3=nums3))