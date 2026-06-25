def findLatestTime(s):
    s = list(s)
    if s[1] != '?':
        if s[1] in ['0','1','2','3']:
            s[0] = '2'
        else:
            s[0] = '1'
    if s[0] != '?':
        if s[0] == '0':
            s[1] = '9'
        elif s[0] == '1':
            s[1] = '1'
        else:
            s[1] = '3'
    if s[3] != '?':
        s[4] = '9'
    if s[4] != '?':
        s[3] = '5'
    return ''.join(s)

print(findLatestTime(s = "1?:?4"))
#partial