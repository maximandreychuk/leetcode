from collections import Counter


def countChars(s: str):
    result, cnt = s[0], 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            result += str(cnt)
            result += s[i]
            cnt = 1
    result += str(cnt)
    return result



print(countChars("AAAABVVKKKKKLL"))
