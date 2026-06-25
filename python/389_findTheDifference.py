from collections import defaultdict
#
# def findTheDifference(s,t):
#     s = [i for i in s]
#     dct1, dct2 = defaultdict(), defaultdict()
#     for i in range(len(s)):
#         if s[i] in dct1.keys():
#             dct1[s[i]] += 1
#         else:
#             dct1[s[i]] = 1
#     for i in range(len(t)):
#         if t[i] in dct2.keys():
#             dct2[t[i]] += 1
#         else:
#             dct2[t[i]] = 1
#     for k, v in dct2.items():
#         try:
#             if dct1[k] != v:
#                 return k
#         except KeyError:
#             return k

def findTheDifference(s, t):
    dct = defaultdict()
    for i in s:
        dct[i] = dct.get(i,0) + 1
    for i in t:
        if i not in dct:
            return i
        elif dct[i] == 0:
            return i
        dct[i]-=1







print(findTheDifference(s = "abcd", t = "abcde"))
print(findTheDifference(s = "a", t = "aa"))