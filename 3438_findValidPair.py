def findValidPair(s):
    counter = {}
    for i in s:
        counter[i] = counter.get(i, 0) + 1
    result = ''
    for k, v in counter.items():
        if int(k) == v:
            result += k
            if len(result) == 2:
                return result
    return ''

print(findValidPair(s="2523533"))
#partial