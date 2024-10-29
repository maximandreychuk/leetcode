def isPowerOfTwo(n):
    for i in range(0,n//2+1):
        if 2**i==n:
            return True
    return False
    # return n > 0 and (n & (n - 1)) == 0

print(isPowerOfTwo(16)) #true
print(isPowerOfTwo(1)) #true
print(isPowerOfTwo(3)) #false