def firstUniqChar(s: str) -> int:
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            return i
    return -1

# s = "leetcode"
# s = "loveleetcode"
s = "aabb"
print(firstUniqChar(s=s))