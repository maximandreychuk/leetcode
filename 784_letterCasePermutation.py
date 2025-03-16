def letterCasePermutation(s):
    l, r = 0, len(s) - 1
    r1, r2 = [], []
    s = list(s)
    while l < r:
        while l < r and not s[l].isalpha():
            l += 1
        while l < r and not s[r].isalpha():
            r -= 1
        if s[l].isupper():
            r1.append(''.join(s))
            s[l] = s[l].lower()
            r1.append(''.join(s))
        else:
            r1.append(''.join(s))
            s[l] = s[l].upper()
            r1.append(''.join(s))
        if s[r].isupper():
            r2.append(''.join(s))
            s[r] = s[r].lower()
            r2.append(''.join(s))
        else:
            r2.append(''.join(s))
            s[r] = s[r].upper()
            r2.append(''.join(s))
        l += 1
        r -= 1
    r = r1+r2

    return r




print(letterCasePermutation(s = "a1b2r")) # ["a1b2","a1B2","A1b2","A1B2"]