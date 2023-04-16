def rotateString(s: str, goal: str) -> bool:
    count = 0
    while count != len(s) and s != goal:
        s = s[1:] + s[0]
        count+=1

    return s == goal


# s = "abcde"
# goal = "cdeab"
s = "abcde"
goal = "abced"
print(rotateString(s, goal))