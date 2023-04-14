def greatestLetter(s: str) -> str:
    dictLower = {}
    dictUpper = {}
    for i in s:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            dictLower[i] = True
        else:
            dictUpper[i] = True
        
    maxValue = "0"
    for k in dictLower:
        if k.upper() in dictUpper and ord(k.upper()) > ord(maxValue):
            maxValue = k.upper()
            
    return maxValue if maxValue != "0" else ""

s = "lEeTcOdE"
print(greatestLetter(s))