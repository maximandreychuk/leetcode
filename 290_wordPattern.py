from collections import defaultdict


def wordPattern(pattern, s):
    pattern, s, dct = [i for i in pattern], s.split(" "), defaultdict()
    if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):
        return False
    for i in range(len(s)):
        if s[i] not in dct.values():
            dct[pattern[i]] = s[i]
    for i in range(len(pattern)):
        if dct[pattern[i]] != s[i]:
            return False
    return True




print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog dog dog dog"))
print(wordPattern("aba", "cat cat cat dog"))