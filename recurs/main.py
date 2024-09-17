step = 0

def persistence(n):
    global step
    lst = [int(i) for i in str(n)]
    if len(lst) == 1:
        return step // 2
    else:
        res = 1 * lst[0]
        lst = lst[1:]
        step += 1
        while len(lst) != 0:
            res = res * lst[0]
            lst = lst[1:]
        return persistence(res)