def repeatedSubstringPattern(s):
    cnt = 1
    while cnt < len(s)//2+1:
        detail = s[:cnt]
        for i in range(len(s)+1):
            add = detail*i
            if add == s:
                return True
        cnt+=1
    return False


# print(repeatedSubstringPattern("abcabcabc"))
print(repeatedSubstringPattern("zzz"))