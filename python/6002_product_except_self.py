def multip(lst1, lst2):
    lst = lst1+lst2
    res = 1
    for i in lst:
        res *= i
    return res

def product_except_self(nums):
    result = []
    i = 0
    while i < len(nums):
        add = multip(nums[0:i], nums[i+1:len(nums)])
        result.append(add)
        i += 1
    return result


print(product_except_self(nums = [1, 2, 3, 4]))