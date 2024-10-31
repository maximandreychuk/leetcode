from collections import defaultdict

def canConstruct(ransomNote, magazine):
    dct = defaultdict()
    for i in range(len(magazine)):
        if magazine[i] in dct.keys():
            dct[magazine[i]] += 1
        else:
            dct[magazine[i]] = 1
    for i in ransomNote:
        try:
            if dct[i] > 0:
                dct[i] -= 1
            else:
                return False
        except KeyError:
            return False
    return True





print(canConstruct("aac", "aabb"))
