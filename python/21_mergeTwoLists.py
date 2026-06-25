def mergeTwoLists(l1, l2):
    if l1 == [0] or l2 == [0]:
        return [0]
    if l1 == [] or l2 == []:
        return []
    res = []
    i = j = 0
    while len(res) != len(l1) + len(l2):
        try:
            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        except:
            res.append(l2[-1])
            return res




print(mergeTwoLists([1, 2, 4,5], [1, 3, 4,6])) # [1, 1, 2, 3, 4, 4]