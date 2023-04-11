def sortSentence(s: str) -> str:
    lst = s.split(" ")
    lstResult = [""] * len(lst)
    for i in lst:
        index = int(i[-1])
        lstResult[index - 1] = i[:len(i)-1]
    
    return " ".join(lstResult)

s = "is2 sentence4 This1 a3"
print(sortSentence(s))