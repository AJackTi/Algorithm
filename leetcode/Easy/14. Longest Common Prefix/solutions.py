def longestCommonPrefix(strs: list[str]) -> str:
    temp = min(word for word in strs)
    i = 0
    while i < len(temp):
        for word in strs:
            if word[i] != temp[i]:
                return temp[0:i]
        i+=1
    return temp

print(longestCommonPrefix(["a", "b"]))