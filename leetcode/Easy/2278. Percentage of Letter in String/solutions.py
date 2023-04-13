import math

def percentageLetter(s: str, letter: str) -> int:
    dictCount = {}
    for i in s:
        if i not in dictCount:
            dictCount[i] = 1
        else:
            dictCount[i] += 1
        
    if letter not in dictCount:
        return 0
    else:
        return math.floor(dictCount[letter] / len(s)*100)
    
print(percentageLetter("foobar", "o"))