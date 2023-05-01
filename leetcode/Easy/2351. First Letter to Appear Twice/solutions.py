def repeatedCharacter(s: str) -> str:
    lookup = set()
    for c in s:
        if c in lookup:
            break
        lookup.add(c)
    return c
        
# s = "abccbaacz"
s = "abcdd"
print(repeatedCharacter(s=s))