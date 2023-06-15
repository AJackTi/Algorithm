def minDays(bloomDay: list[int], m: int, k: int) -> int:
    left = 0
    right = max(bloomDay)
    ans = -1

    def calcBouquets(dayAt):
        nBouquets = 0
        nAdjFlowers = 0
        for d in bloomDay:
            if dayAt >= d:
                nAdjFlowers += 1
            else:
                nBouquets += nAdjFlowers // k
                nAdjFlowers = 0
        
        nBouquets += nAdjFlowers // k
        return nBouquets
    
    while left <= right:
        mid = (left + right) // 2
        if calcBouquets(mid) >= m:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
        
    return ans