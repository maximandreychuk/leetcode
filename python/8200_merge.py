def merge(intervals: list[list[int]]) -> list[list[int]]:
    result: list = []
    for i in range(1, len(intervals)):
        if result:
            rule_1 = result[-1][0] <= result[-1][0]
            rule_2 = result[-1][1] >= intervals[i][0]
            rule_3 = intervals[i][0] <= intervals[i][1]
            if rule_1 and rule_2 and rule_3:
                result = result[:-1]
                result.append([add, intervals[i][1]])
                i += 1
            else:
                result.append(intervals[i])
        else:
            rule_1 = intervals[i-1][0] <= intervals[i-1][0]
            rule_2 = intervals[i-1][1] >= intervals[i][0]
            rule_3 = intervals[i][0] <= intervals[i][1]
            if rule_1 and rule_2 and rule_3:
                result.append([intervals[i-1][0], intervals[i][1]])
                i += 1
    return result

print(merge([[1,3],[2,6],[8,10],[9,11],[15,18],[17,20]] ))