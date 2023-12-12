def isAcronym(words: list[str], s: str) -> bool:
    if len(words) != len(s):
        return False
    
    for i in range(0, len(words)):
        if words[i][0] != s[i]:
            return False

    return True