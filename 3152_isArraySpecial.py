def isArraySpecial(nums, queries):
    result = []
    for i in queries:
        subarr = nums[i[0]:i[1]+1]
        for j in range(1, len(subarr)):
            flag = False
            if subarr[j] % 2 == 0 and subarr[j-1] % 2 == 0:
                result.append(False)
                flag = True
                break
            if subarr[j] % 2 != 0 and subarr[j-1] % 2 != 0:
                result.append(False)
                flag = True
                break
        if not flag:
            result.append(True)
    return result

print(isArraySpecial([3,4,1,2,6], queries = [[0,4]]))
#partial
#Time Limit Exceeded 535 / 536 testcases passed
