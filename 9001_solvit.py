def reverse_string(s: list[str]):
    mid = len(s) // 2
    for i in range(mid):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
    return s

print(reverse_string(['g','h','r']))