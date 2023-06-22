def maxProfit(prices: list[int], fee: int) -> int:
    length = len(prices)
    profit = 0
    effectiveBuyPrice = prices[0]
    
    for i in range(1, length):
        profit = max(profit, prices[i] - effectiveBuyPrice - fee)
        effectiveBuyPrice = min(effectiveBuyPrice, prices[i] - profit)
    
    return profit

prices = [1,3,2,8,4,9]
fee = 2

print(maxProfit(prices=prices, fee=fee))