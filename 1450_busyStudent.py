def busyStudent(startTime, endTime, queryTime):
    i = cnt = 0
    while i < len(startTime):
        numbers = [numb for numb in range(startTime[i], endTime[i]+1)]
        if queryTime in numbers:
            cnt += 1
        i += 1
    return cnt

print([_ for _ in range(1,2)])



print(busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4)) # 1