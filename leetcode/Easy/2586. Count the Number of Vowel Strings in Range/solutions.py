def vowelStrings(words: list[str], left: int, right: int) -> int:
    vowel_characters = ['a', 'e', 'i', 'o', 'u']
    ans = 0
    for i in words[left : right + 1]:
        if i[0] in vowel_characters and i[-1] in vowel_characters:
            ans += 1

    return ans

words = ["are","amy","u"]
left = 0
right = 2
print(vowelStrings(words, left, right))