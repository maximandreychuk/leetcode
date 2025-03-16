def numEquivDominoPairs(dominoes):
    record = 0
    head = 1
    while head < len(dominoes):
        new_record = 0
        for i in range(head, len(dominoes)):
            if dominoes[i]==dominoes[i-1] or dominoes[i][0]==dominoes[i-1][1] and dominoes[i][1]==dominoes[i-1][0]:
                record += 1
        if new_record > record:
            record = new_record
        head += 1
    # if dominoes[-1] == dominoes[-2] or dominoes[-1][0] == dominoes[-2][1] and dominoes[-1][1] == dominoes[-2][0]:
    #     record += 1
    return record


print(numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))