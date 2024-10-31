from collections import defaultdict, Counter, OrderedDict

def isSubsequence(s,t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return len(s) == i




print(isSubsequence(s = "abc", t = "ahbgdc")) # true
print(isSubsequence(s = "axc", t = "ahbgdc"))
print(isSubsequence(s = "abc", t = ""))
print(isSubsequence(s = "acb", t = "ahbgdc"))