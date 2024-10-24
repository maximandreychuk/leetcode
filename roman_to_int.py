

dct = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

#XXIIVII 26
def romanToInt(s: str) -> int:
    cnt = 0
    for i,j in zip(s, s[1:]):
        if i == "I" and j in ["V", "X"]:
            cnt -= 1
        elif i == "I" and j in ["L", "C"]:
            cnt -= 10
        elif i == "I" and j in ["D", "M"]:
            cnt -= 100
        else:
            cnt += dct[i]
    cnt += dct[s[-1]]
    return cnt



print(romanToInt("XXIIVIIX"))
print(romanToInt("MCMXCIV"))
print(romanToInt("IIIXCLIVIIX"))