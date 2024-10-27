def generate(n):
    base = [[1], [1,1],]
    for i in range(1, n-1):
        base.append([1])
        for j in range(len(base[i])):
            if j < len(base[i])-1:
                base[i+1].append(base[i][j] + base[i][j+1])
            else:
                base[i+1].append(1)
    return base



print(generate(5)) # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


