def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    return ''.join(word1) == ''.join(word2)


word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1, word2))
