def findSpecialInteger(arr: list[int]) -> int:
    for i in arr:
        if arr.count(i) > len(arr) / 4:
            return i

arr = [1,2,2,6,6,6,6,7,10]
print(findSpecialInteger(arr))