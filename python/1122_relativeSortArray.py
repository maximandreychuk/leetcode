def relativeSortArray(arr1, arr2):
    i = 0
    res = []
    add = []
    while i < len(arr2):
        for j in arr1:
            if j == arr2[i]:
                res.append(j)
            elif j not in arr2:
                if j not in add:
                    add.append(j)
        i += 1
    return res + sorted(add)



print(relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))

