def arrayRankTransform(arr):
    dct = {}
    result = []
    sort_arr = sorted(arr)
    for i in range(len(sort_arr)):
        if sort_arr[i] not in dct.keys():
            dct[sort_arr[i]] = i
        else:
            dct[sort_arr[i]] = dct[sort_arr[i]]
    for i in arr:
        result.append(dct[i]+1)
    print(dct)
    return result



print(arrayRankTransform(arr = [37,12,28,9,100,56,80,5,12])) # [5,3,4,2,8,6,7,1,3]