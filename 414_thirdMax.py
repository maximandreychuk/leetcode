def thirdMax(nums):
    first = second = third = float("-inf")
    for i in nums:
        if i > first:
            third = second
            second = first
            first = i
        elif first > i and  i > second and i != first:
            third = second
            second = i
        elif i < second and i > third and i != first and i != second:
            third = i
    if third != float("-inf"):
        return third
    return first






print(thirdMax([3,2,1]))
print(thirdMax([2,2,3,1]))
print(thirdMax([1,2]))
