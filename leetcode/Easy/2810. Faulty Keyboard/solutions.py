def finalString(s: str) -> str:
    ans = ""
    for i in range(0, len(s)):
        if s[i] == "i":
            ans = ans[::-1]
        else:
            ans += s[i]

    return ans

print(finalString("string"))