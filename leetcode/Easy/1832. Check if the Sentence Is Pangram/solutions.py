def checkIfPangram(sentence: str) -> bool:
    return set("abcdefghijklmnopqrstuvwxyz") == set(sentence)

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence=sentence))