from collections import Counter, defaultdict


def intersect(num1, num2):
    dct1 ,dct2 = Counter(num1), Counter(num2)
    r = []
    for i in dct1:
        if i in dct2:
            r.extend([i]*min(dct1[i], dct2[i]))
    return r




print(intersect(num1 = [4,9,5], num2 = [9,4,9,8,4]))
