def minimumAbsDifference(arr):
    arr.sort()
    min_diff = arr[1] - arr[0]
    result = []
    for i in range(len(arr) - 1):
        min_diff = min(min_diff, arr[i+1] - arr[i])
    for i in range(len(arr) - 1):
        if arr[i+1] - arr[i] == min_diff:
            result.append(sorted([arr[i+1], arr[i]]))
    return result


print(minimumAbsDifference([4,2,1,3])) # [[1,2],[2,3],[3,4]]