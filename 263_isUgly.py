def isUgly(n):
    pm=[2,3,5]
    if n <= 0:
        return False
    for p in pm:
        while n%p==0:
            n//=p
    return n==1

print(isUgly(14)) # false
print(isUgly(16))
print(isUgly(6))
print(isUgly(8))
print(isUgly(1))
print(isUgly(13)) # false