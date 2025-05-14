from django.db.models.expressions import result


def interval(arr):
    arr = [i for i in arr]
    print(arr)
    result = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] == 1:
            result.append(str(arr[i-1]))
        else:
            result.append(f"{arr[i - 1]}-{arr[i]}")
    return result


print(interval([1,2,4,5,8])) # [1, 2, 4-5, 5-8]