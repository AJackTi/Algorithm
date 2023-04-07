def isAnagram(s: str, t: str) -> bool:
    dictS = {}
    for i in sorted(s):
        if i not in dictS:
            dictS[i] = 1
        else:
            dictS[i] += 1

    dictT = {}
    for i in sorted(t):
        if i not in dictS:
            return False
        if i not in dictT:
            dictT[i] = 1
        else:
            dictT[i] += 1
    
    return dictS == dictT