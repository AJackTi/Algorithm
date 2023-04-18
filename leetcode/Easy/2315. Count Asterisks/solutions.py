def countAsterisks(s: str) -> int:
    count = 0
    lstS = list(s)
    lstVerticalBars = [i for i, e in enumerate(list(s)) if e == "|"]
    res = [(i, (i + 1)) for i in range(1, len(lstVerticalBars))]
    for i in range(len(res)):
        if i % 2 != 0:
            count += s[lstVerticalBars[res[i][0] - 1]: lstVerticalBars[res[i][1] - 1] + 1].count('*')
        
    return count

s = "*||*|||||*|*|***||*||***|"
print(countAsterisks(s))