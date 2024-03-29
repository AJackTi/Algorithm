def mySqrt(self, x: int) -> int:
    left = 0
    right = 46340
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans    