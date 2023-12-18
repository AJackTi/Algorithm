def sortByBits(arr: list[int]) -> list[int]:
    ans = []
    count = 0
    for i in arr:
        count = 0
        for j in range(0, 32):
            if i & (1 << j):
                count += 1
        ans.append((count, i))
    ans.sort()

    return [i[1] for i in ans]

print(sortByBits([0,1,2,3,4,5,6,7,8]))