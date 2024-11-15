def addToArrayForm(num, k):
    return [int(i) for i in str(int("".join([str(i) for i in num])) + k)]





print(addToArrayForm(num = [2,7,4], k = 181)) # 455