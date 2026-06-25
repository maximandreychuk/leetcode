def buttonWithLongestTime(events):
    result = events[0][1]
    for i in range(1, len(events)):
        if events[i][1] - events[i-1][1] > result:
            result = events[i][0]
    return result

print(buttonWithLongestTime(events = [[1,2],[2,5],[3,9],[1,15]]))
#partial


