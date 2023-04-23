def numJewelsInStones(jewels: str, stones: str) -> int:
    jewelsSet = set(jewels)
    return sum(stone in jewelsSet for stone in stones)


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels=jewels, stones=stones))