def generateTheString(n):
    new_n = ""
    if n % 2 == 0:
        for i in range(n-1):
            new_n += "a"
        new_n += "b"
        return new_n
    else:
        for i in range(n):
            new_n += "a"
        return new_n

print(generateTheString(4))