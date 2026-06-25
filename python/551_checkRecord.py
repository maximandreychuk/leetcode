def checkRecord(s):
    a = l = 0
    start = end = 1
    for i in range(1, len(s)):
        if s[i-1] == "A":
            a += 1
        if s[i-1] == "L":
            if end - start == 3:
                l += 1
            else:
                end += 1
        else:
            start = end = 1
    if s[-1] == "L":
        end += 1
        if end - start == 3:
            l += 1
    if s[-1] == "A":
        a += 1
    print(a, l)
    return True if a < 2 and l < 2 else False



print(checkRecord("PPALLL")) # false
print(checkRecord("PPALLP")) # true
print(checkRecord("AAAAA")) # false