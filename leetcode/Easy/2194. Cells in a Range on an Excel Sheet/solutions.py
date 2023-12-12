def cellsInRange(s: str) -> list[str]:
    lst_s = s.split(":")
    ans = []
    for c in range(ord(lst_s[0][0]), ord(lst_s[1][0])+1):
        for num in range(int(lst_s[0][1:]), int(lst_s[1][1:])+1):
            ans.append(chr(c) + str(num))

    return ans

# print(cellsInRange("K1:L2"))
print(cellsInRange("A1:F1"))