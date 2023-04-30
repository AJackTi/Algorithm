def sumBase(n: int, k: int) -> int:
    ans = 0
    
    while n > 0:
        ans += (n%k)
        n //= k
    
    return ans

n = 34
k = 6
print(sumBase(n=n, k=k))