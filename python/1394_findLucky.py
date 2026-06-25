def findLucky(arr):
    dct = {}
    for i in arr:
        if i not in dct.keys():
            dct[i] = 1
        else:
            dct[i] += 1
    m = float("-inf")
    for k, v in dct.items():
        if k == v and k > m:
            m = k
    return m if m != float("-inf") else -1



print(findLucky(arr = [2,2,3,4]))
