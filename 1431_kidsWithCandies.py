def kidsWithCandies(candies, extraCandies):
    max_candies, result = max(candies), []
    for i in candies:
        if i + extraCandies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result

print(kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))