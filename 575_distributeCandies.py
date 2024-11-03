from collections import Counter

def distributeCandies(candyType):
    d = Counter(candyType)
    res = 0
    for _ in d.keys():
        if res >= len(candyType)//2:
            return res
        res+=1
    return res



print(distributeCandies([6,6,6,6]))
print(distributeCandies([1,1,2,2,3,3]))
print(distributeCandies([1,1,2,3]))