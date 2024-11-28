def maxPower(s):
    max_score = 1
    cnt = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            cnt = 1
        else:
            cnt += 1
        max_score = max(max_score, cnt)
    return max_score



print(maxPower(s = "leetcode")) # 2
print(maxPower(s = "abbcccddddeeeeedcba"))
