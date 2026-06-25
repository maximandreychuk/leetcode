from string import ascii_lowercase as asc

def nextGreatestLetter(letters, target):
    dct = {}
    for i in range(len(asc)):
        dct[asc[i]] = i
    for i in range(len(letters)):
        if dct[letters[i]] > dct[target]:
            return letters[i]
    return letters[0]



print(nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(nextGreatestLetter(letters = ["c","f","j"], target = "c"))