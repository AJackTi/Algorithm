def countConsistentStrings(allowed: str, words: list[str]) -> int:
    count = 0
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] not in allowed:
                break
        else:
            count += 1
    return count

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(countConsistentStrings(allowed, words))