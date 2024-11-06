def numJewelsInStones(jewels, stones):
    counter, dct = 0, {}
    for i in stones:
        if i not in dct.keys():
            dct[i] = 1
        else:
            dct[i] += 1
    for i in jewels:
        if i in dct.keys():
            counter += dct[i]
    return counter


print(numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(numJewelsInStones(jewels = "z", stones = "ZZ"))