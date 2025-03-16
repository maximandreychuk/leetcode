def findXSum(nums, k, x):
    result = []
    for i in range(len(nums)):
        if i+k <= len(nums):
            subarray = nums[i:i+k]
            dict = {}
            for j in subarray:
                dict[j] = dict.get(j, 0) + 1
            sorted_dict = sorted(dict.items(), key = lambda item: (item[1], item[0]))
            summa = 0
            for el in range(1, x+1):
                summa+=sorted_dict[-el][0]*sorted_dict[-el][1]
            result.append(summa)
        else:
            return result

print(findXSum(nums = [1,1,2,2,3,4,2,3], k = 6, x = 2))
#partially
