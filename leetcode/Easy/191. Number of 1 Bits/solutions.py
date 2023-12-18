def hammingWeight(n: int) -> int:
    count = 0
    while n != 0:
        print('n', n)
        print('n-1', n-1)
        print('n & (n-1)', n & (n-1))
        n = n & (n-1)
        count += 1
    return count

n = 0o00000000000000000000000000001011
hammingWeight(n=n)