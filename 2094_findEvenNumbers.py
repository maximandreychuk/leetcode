def findEvenNumbers(nums):
    res = []
    for i in nums:
        for j in nums:
            for k in nums:
                if i != k and i != j:
                    if i != 0 and i != j != k:
                        n = int(f"{i}{j}{k}")
                        if n % 2 == 0:
                            res.append(int(f"{i}{j}{k}"))
    return res




print(findEvenNumbers([2,1,3,0]))
# [102,120,130,132,210,230,302,310,312,320]