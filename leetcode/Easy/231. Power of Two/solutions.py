import math

def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    return 2 ** int(math.log2(n)) == n

n = 0
print(isPowerOfTwo(n=n))