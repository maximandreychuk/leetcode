def addDigits(n):
    if len(str(n)) == 1:
        return n
    n = [int(i) for i in str(n)]
    nn=0
    for j in range(len(n)):
        nn+=n[j]
    return addDigits(nn)



print(addDigits(101))