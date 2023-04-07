import math

def mergedSortedArrays(nums1, nums2):
    combined = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            combined.append(nums1[i])
            i+=1
        else:
            combined.append(nums2[j])
            j+=1
    
    while i < len(nums1):
        combined.append(nums1[i])
        i+=1

    while j < len(nums2):
        combined.append(nums2[j])
        j+=1
    
    return combined

def findMedianSortedArrays(nums1, nums2) -> float:
    combined = mergedSortedArrays(nums1, nums2)
    print(combined)
    if len(combined) % 2 == 0:
        first = combined[int(len(combined) / 2 - 1)]
        last = combined[int(len(combined) / 2)]
        return (first + last) / 2
    else:
        return (combined[math.floor(len(combined) / 2)])
    
print(findMedianSortedArrays([1,3], [2]))