def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    combined = []
    i, j = 0,0
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            combined.append(nums1[i])
            i+=1
        else:
            combined.append(nums2[j])
            j+=1
        
    while i < m:
        combined.append(nums1[i])
        i+=1

    while j < n:
        combined.append(nums2[j])
        j+=1

    nums1 = combined

merge([1,2,3,0,0,0], 3, [2,5,6], 3)