def finalPrices(prices):
    i = 0
    j = 1
    result = []
    while i < len(prices):
        check = len(result)
        for n in range(j, len(prices)):
            if prices[n] <= prices[i]:
                result.append(prices[i]-prices[n])
                break
        if len(result) == check:
            result.append(prices[i])
        i += 1
        j += 1
    return result


print(finalPrices(prices = [8,4,6,2,3])) # [4,2,4,2,3]
print(finalPrices([10,1,1,6]))
print(finalPrices([1,2,3,4,5]))