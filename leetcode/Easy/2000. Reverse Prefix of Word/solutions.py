def reversePrefix(word: str, ch: str) -> str:
    if not ch in word:
        return ""
    
    idxFirst = word.index(ch)
    reversedWord = word[0:idxFirst+1][::-1]
    
    return reversedWord + word[idxFirst+1:len(word)]

word = "abcdefd"
ch = "d"
print(reversePrefix(word, ch))