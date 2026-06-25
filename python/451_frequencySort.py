def isFreq(s):
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    sort = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    result = ""
    for item in sort:
        result += f"{item[0]*item[1]}"
    return result


print(isFreq("bbAa"))
