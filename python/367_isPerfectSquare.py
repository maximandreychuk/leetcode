def isPerfectSquare(n):
    if n == 1:
        return True
    for i in range(n):
        if i*i>n:
            return False
        if i*i == n:
            return True


print(isPerfectSquare(27))
print(isPerfectSquare(16))
print(isPerfectSquare(2000105819))