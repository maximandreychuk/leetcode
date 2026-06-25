def reverseStr(s, k):
    start, end, flag, res = 0, k, 2, ""
    while start < len(s):
        if flag % 2 == 0:
            res += s[start:end][::-1]
            start += k
            end += k
            flag+=1
        else:
            res += s[start:end]
            start += k
            end += k
            flag+=1
    return res


print(reverseStr(s = "abcdefg", k = 2))
print(reverseStr(s = "1234567890", k = 2))
print(reverseStr(s = "abcd", k = 2))