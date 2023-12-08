def findWordsContaining(words: list[str], x: str) -> list[int]:
    res = []
    for i in range(len(words)):
        if x in words[i]:
            res.append(i)
    return res