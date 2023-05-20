def lengthOfLastWord(s: str) -> int:
    return len(s.strip().split(" ")[-1])

# s = "Hello World"
s = "   fly me   to   the moon  "
print(lengthOfLastWord(s=s))