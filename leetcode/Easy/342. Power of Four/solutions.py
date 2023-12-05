def isPowerOfFour(n: int) -> bool:
    count = 0
    while True:
        if 4 ** count == n:
            return True
        if 4 ** count > n:
            return False
        count += 1

print(isPowerOfFour(5))