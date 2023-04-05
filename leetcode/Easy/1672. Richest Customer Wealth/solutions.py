def maximumWealth(accounts: list[list[int]]) -> int:
    max = 0
    for i in accounts:
        if sum(i) > max:
            max = sum(i)
    
    return max

accounts = [[1,5],[7,3],[3,5]]
max = maximumWealth(accounts=accounts)
print(max)