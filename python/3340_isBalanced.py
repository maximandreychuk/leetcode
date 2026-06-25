def isBalanced(num):
    even = odd = 0
    flag = True
    for i in range(0, len(num)):
        if flag:
            even += int(num[i])
            flag = False
        else:
            odd += int(num[i])
            flag=True
    return even == odd

print(isBalanced('1234'))
#done