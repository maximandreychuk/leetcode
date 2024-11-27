def maxScore(s):
    max_score = float("-inf")
    flag = 1
    while flag < len(s)-1:
        sum1 = len([i for i in s[0:flag] if i == "0"])
        sum2 = len([i for i in s[flag:len(s)] if i == "1"])
        new_max_score = sum1 + sum2
        if new_max_score > max_score:
            max_score = new_max_score
        flag += 1
    return max_score


# print(maxScore(s = "011101")) # 5
# print(maxScore(s = "00111")) # 5
print(maxScore(s = "000"))