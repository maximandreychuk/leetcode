def maxProfit(prices):
    if len(prices)<2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in range(1, len(prices)):
        if prices[price] < min_price:
            min_price = prices[price]
        elif max_profit < prices[price] - min_price:
            max_profit =  prices[price] - min_price
    return max_profit




print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1]))


