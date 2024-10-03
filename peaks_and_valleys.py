# Task & Rules
# Give you an array arr that contains some number elements, find out the peaks
# and valleys in the array, and return them.
#
# What do the peaks and valleys mean? If an element is
# larger than the three one on the left and larger than the three one on the right, we call it a peak. In contrast, an element is smaller than the value of the three elements(left and right), we call it a valley. an example:
#
# [10,20,30,40,30,20,10,11,12,13,14,15,16,15,14,13]
# In the example above, peaks and valleys are:
#
# [10,20,30,40,30,20,10,11,12,13,14,15,16,15,14,13]
#
# [         40   ,   10        ,       16         ]

# peakAndValley([10,20,30,40,30,20,10,11,12,13,14,15,16,15,14,13])
# should return [40,10,16]

def peak_and_valley(arr):
    arr = [0,0,0] + arr + [0,0,0]
    res = []
    for idx in range(3, len(arr)-3):
        if arr[idx] < min(arr[idx-3],arr[idx-2],arr[idx-1]) and arr[idx] < min(arr[idx+3],arr[idx+2],arr[idx+1]):
            res.append(arr[idx])
        elif arr[idx] > max(arr[idx-3],arr[idx-2],arr[idx-1]) and arr[idx] > max(arr[idx+3],arr[idx+2],arr[idx+1]):
            res.append(arr[idx])
    return res

print(peak_and_valley([10,20,30,40,30,20,10,11,12,13,14,15,16,15,14,13]))
print(peak_and_valley([31, 99, 2, 92, 19, 60]))