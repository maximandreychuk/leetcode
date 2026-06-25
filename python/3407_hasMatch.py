def hasMatchs(s, p):
    start_idx = 0
    for i in range(len(p)):
        if p[i] == '*':
            start_idx = i
    prefix = p[:start_idx]
    suffix = p[start_idx+1:]
    for i in range(len(s)-len(p)+1):
        if s[i:len(prefix)+1] == prefix and s[i+len(prefix):].endswith(suffix):
            return True
    return False


print(hasMatchs(s = "leetcode", p = "ee*e"))
print(hasMatchs(s = "car", p = "c*v"))