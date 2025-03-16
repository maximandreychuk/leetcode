def constructRectangle(area):
    result = []
    for i in range(1, area+1):
        for j in range(1,area+1):
            if len(result) == 0:
                result.append([i, j])
            elif i == j and result[0][0] == result[0][1]:
                if i > result[0][0]:
                    result[0][0], result[0][1] = i, j
            elif i >= j and result[0][0]-result[0][0]>i-j:
                result.append([i,j])
    return result


print(constructRectangle(4)) # [2,2]
# print(constructRectangle(122122)) # [427,286]