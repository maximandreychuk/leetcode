def getSneakyNumbers(nums):
    dct = {}
    result = []
    for i in nums:
        if i in dct.keys():
            dct[i] += 1
            result.append(i)
            if len(result) == 2:
                return result
        else:
            dct[i] = 1
    return result

print(getSneakyNumbers(nums = [7,1,5,4,3,4,6,0,9,5,8,2]))
#done