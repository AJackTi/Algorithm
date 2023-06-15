def arrangeCoins(n: int) -> int:
    left = 1
    # right = n
    right = int(sqrt(2*n+1/4) + 1/2)
    ans = 1

    def calcCoinsRequired(r):
        # 1 + 2 + 3 + ... + r
        # r * (r + 1) / 2
        return r * (r + 1) // 2

    while left <= right:
        mid = (left + right) // 2
        nCoinsRequired = calcCoinsRequired(mid)
        if n >= nCoinsRequired:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
            
    return ans