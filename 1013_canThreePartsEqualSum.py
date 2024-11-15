def canThreePartsEqualSum(arr):
    if len(arr) < 3:
        return False
    a,b,n = 1,2,len(arr)
    step = 3
    while step < n-3:
        aa, bb = a, b
        while b < n:
            if sum(arr[0:a]) == sum(arr[a:b]) == sum(arr[b:n]):
                return True
            else:
                b += 1
        a, b = aa, bb
        a += 1
        b += 1
        step += 1
    return False


print(canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))