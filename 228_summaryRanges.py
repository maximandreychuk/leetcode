
def summaryRanges(nums):
    if nums == []:
        return []
    start = end = 0
    result = []
    for i in range(1, len(nums)):
        if nums[i] - nums[i-1] == 1:
            end += 1
        else:
            if start == end:
                result.append(str(nums[start]))
            else:
                result.append(f"{start}->{end}")
            start = end = i
    if start == end:
        result.append(str(nums[start]))
    else:
        result.append(f"{start}->{end}")
    return result


print(summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]
print(summaryRanges([0,2,3,4,6,8,9]))  # ["0","2->4","6","8->9"]