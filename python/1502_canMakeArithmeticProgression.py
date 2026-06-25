def canMakeArithmeticProgression(arr):
    arr.sort()
    diff = arr[1]-arr[0]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False
    return True



print(canMakeArithmeticProgression([3,5,1])) # true
print(canMakeArithmeticProgression(arr = [1,2,4])) # false