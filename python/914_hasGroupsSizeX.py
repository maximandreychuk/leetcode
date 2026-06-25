def hasGroupsSizeX(deck):
    if len(deck) < 2:
        return False
    dct = {}
    for i in range(len(deck)):
        if deck[i] not in dct.keys():
            dct[deck[i]] = 1
        else:
            dct[deck[i]] += 1
    m = min(dct.values())
    if m % 2 == 0:
        for i in dct.values():
            if i % 2 != 0:
                return False
    else:
        for i in dct.values():
            if i != m:
                return False
    return True



print(hasGroupsSizeX(deck = [1,2,3,4,4,3,2,1]))
print(hasGroupsSizeX(deck = [1,2,3,4,2,3,2,1]))
print(hasGroupsSizeX(deck = [1,1,2,2,2,2,3,3,3,3,3,3]))