def smallestNumber(n, t):
    while True:
        v = n
        n = [i for i in str(n)]
        mul = int(n[0])
        for i in range(1, len(n)):
            mul *= int(n[i])
        if mul % t == 0:
            return v
        n = v + 1

print(smallestNumber(15, 3))