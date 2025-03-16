def destCity(paths):
    start = paths[0][0]
    end = paths[0][1]
    for i in range(1, len(paths)):
        if paths[i][0] == end:
            start = paths[i][0]
            end = paths[i][1]
    return end



print(destCity(paths = [["B","C"],["D","B"],["C","A"]])) # A