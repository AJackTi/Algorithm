def truncateSentence(s: str, k: int) -> str:
    output = s.split(' ')
    return ' '.join(output[:k])

s = "Hello how are you Contestant"
k = 4
output = truncateSentence(s, k)
print(output)