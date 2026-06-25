from collections import defaultdict

def palindromePermutation(s):
    dct = defaultdict()
    for i, ch in enumerate(s):
        if ch in dct:
            dct[ch] += 1
        else:
            dct[ch] = 1
    cnt = 0
    for v in dct.values():
        if v % 2 != 0:
            cnt += 1
    if cnt > 1:
        return False
    return True

# ecod deco odec, ceod cdeo, coed
print(palindromePermutation("code")) # false
print(palindromePermutation("carerac")) # true
print(palindromePermutation("aab")) # true
