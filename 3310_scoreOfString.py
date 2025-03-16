def scoreOfString(s):
    result = 0
    for i in range(1, len(s)):
        result += abs(ord(s[i-1]) - ord(s[i]))
    return result


print(scoreOfString('hello'))
#done