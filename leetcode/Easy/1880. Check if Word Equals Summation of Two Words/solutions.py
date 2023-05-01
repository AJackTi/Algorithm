def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def stoi(s):
        result = 0
        for c in s:
            result = result*10 + ord(c)-ord('a')
        return result
    
    return stoi(firstWord) + stoi(secondWord) == stoi(targetWord)

firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
# firstWord = "aaa"
# secondWord = "a"
# targetWord = "aab"
print(isSumEqual(firstWord=firstWord, secondWord=secondWord, targetWord=targetWord))