def isValid(word):
    if len(word) < 3:
        return False
    coins = [0,0,0]
    for i in word:
        if i.isdigit() and coins[0] != 1:
            coins[0] = 1
        if i.isalpha() and i in ('a', 'e', 'i', 'o', 'u') and coins[1] != 1:
            coins[1] = 1
        if i.isalpha() and i not in ('a', 'e', 'i', 'o', 'u') and coins[2] != 1:
            coins[2] = 1
    return coins[0] == coins[1] == coins[2] == True


print(isValid(word = "Adas"))
#partial