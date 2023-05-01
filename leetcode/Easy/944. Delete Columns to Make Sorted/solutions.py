def minDeletionSize(strs: list[str]) -> int:
    result = 0
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if strs[j-1][i] > strs[j][i]:
                result += 1
                break
    return result

strs = ["cba","daf","ghi"]
print(minDeletionSize(strs=strs))