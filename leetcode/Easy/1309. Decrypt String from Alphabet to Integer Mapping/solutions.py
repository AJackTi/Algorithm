def freqAlphabets(s: str) -> str:
    m = {}
    x = 'a'
    for i in range(1, 27):
        m[str(i)] = x
        x = chr(ord(x) + 1)
    ans = ""
    m['']=''
    i = len(s) - 1
    while i >= 0:
        if s[i] == "#":
            temp = ""
            for j in range(i - 2, i):
                temp += s[j]
            ans = m[str(temp)] + ans
            i -= 3
        else:
            ans = m[s[i]] + ans
            i -= 1
    return ans

# s = "10#11#12"
s = "1326#"
print(freqAlphabets(s=s))