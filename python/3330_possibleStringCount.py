def possibleStringCount(word):
    cnt = 1
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            cnt += 1
    return cnt

print(possibleStringCount(word = "aaaa"))
#done