def findContentChildren(g, s):
    cookie_idx = child_idx = result = 0
    child = sorted(g)
    cookie = sorted(s)
    while child_idx < len(child) and cookie_idx < len(cookie):
        if child[child_idx] <= cookie[cookie_idx]:
            child_idx += 1
            result += 1
        cookie_idx += 1
    return result


print(findContentChildren([1,2,3], [1,2]))