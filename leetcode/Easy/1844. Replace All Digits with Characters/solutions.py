def replaceDigits(s: str) -> str:
    ans = ''
    for i in range(0, len(s), 2):
        if i+1 == len(s):
            return ans + s[i]
        ans += s[i] + chr(ord(s[i]) + int(s[i+1]))
    
    return ans

# s = "a1c1e1"
s = "a1b2c3d4e"
print(replaceDigits(s))