def totalMoney(n: int) -> int:
    ans = 0
    for idx in range(0, n//7):
        ans += sum(range(1+idx, 8+idx))

    extra = n - n//7*7
    
    return ans + sum(range(n//7 + 1,n//7+extra+1))

# print(totalMoney(4))
# print(totalMoney(10))
print(totalMoney(20))