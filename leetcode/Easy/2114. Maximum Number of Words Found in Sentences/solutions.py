def mostWordsFound(sentences: list[str]) -> int:
    max = 0
    for i in sentences:
        if len(i.split()) > max:
            max = len(i.split())
            
    return max

print(mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"]))