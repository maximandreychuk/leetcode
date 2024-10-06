# Task
# Write a function that accepts a list that can contain missing data,
# and an integer representing the method on how to fill the missing data
# if there is any. Missing data is represented as None.
# The list will only contain integers and None values.
#
# Note that depending on the language you attempt this kata with,
# None corresponds to:
#
# None (Python)
# undefined (Javascript)
# The fill method rules are outlined below:
#
# Fill method:
#   -1: backwards
#    0: nearest
#    1: forwards
# Example
arr = [None, 1, None, None, None, 2, None]
#
# fill(arr, -1) == [1, 1, 2, 2, 2, 2, None]  # None replaced by closest int on the right
# fill(arr,  0) == [1, 1, 1, 1, 2, 2, 2]     # None replaced by closest int. If equidistant, choose the smallest int
# fill(arr,  1) == [None, 1, 1, 1, 1, 2, 2]  # None replaced by closest int on the left


def fill(arr, method):
    if arr == []:
        return []
    elif arr == [None]:
        return [None]
    elif method == -1:
        for idx in range(len(arr)-1, -1, -1):
            if arr[idx] != None:
                rest = arr[idx:]
                arr = arr[:idx+1]
                break
        fill = arr[-1]
        for idx in range(len(arr) - 2, -1, -1):
            if arr[idx] == None:
                arr[idx] = fill
            else:
                fill = arr[idx]
        return arr+rest
    elif method == 1:
        for idx in range(0, len(arr)):
            if arr[idx] != None:
                rest=arr[:idx]
                arr=arr[idx:]
                break
        fill=arr[0]
        for idx in range(0,len(arr)):
            if arr[idx] == None:
                arr[idx] = fill
            else:
                fill=arr[idx]
        return rest+arr
    elif method == 0:
        filled_arr = []
        for i in range(len(arr)):
            if arr[i] is not None:
                filled_arr.append(arr[i])
            else:
                left_index = i - 1
                right_index = i + 1

                while left_index >= 0 and arr[left_index] is None:
                    left_index -= 1

                while right_index < len(arr) and arr[right_index] is None:
                    right_index += 1

                if left_index < 0:
                    filled_arr.append(arr[right_index])
                elif right_index >= len(arr):
                    filled_arr.append(arr[left_index])
                elif abs(i - left_index) <= abs(right_index - i):
                    filled_arr.append(arr[left_index])
                else:
                    filled_arr.append(arr[right_index])
        return filled_arr








print(fill(arr , -1))
print(fill(arr, 0))
print(fill(arr, 1))
