from collections import defaultdict


def firstUniqChar(s):
    dct = defaultdict()
    for i in range(len(s)):
        if s[i] in dct.keys():
            dct[s[i]][0] += 1
        else:
            dct[s[i]] = [1, i]
    for l in dct.values():
        if l[0] ==1:
            return l[1]
    return -1

print(firstUniqChar("loveleetcode"))

