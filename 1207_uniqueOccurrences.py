def uniqueOccurrences(arr):
    dct = {}
    for i in range(len(arr)):
        if arr[i] not in dct.keys():
            dct[arr[i]] = 1
        else:
            dct[arr[i]] += 1
    for k1, i in dct.items():
        for k2, j in dct.items():
            if k1 != k2:
                if i == j:
                    return False
    return True

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))
print(uniqueOccurrences([1,2]))