def halvesAreAlike(s: str) -> bool:
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    return len([i for i in s[:len(s)//2] if i in vowels]) == len([i for i in s[len(s)//2:] if i in vowels])

s = "book"
print(halvesAreAlike(s=s))