def maxScoreSightseeingPair(values):
    sum = float("-inf")
    tail, head = 0, 1
    while head < len(values):
        for i in range(head, len(values)):
            if values[tail] + values[i] + tail - i > sum:
                sum = values[tail] + values[i] + tail - i
        tail += 1
        head += 1
    return sum



print(maxScoreSightseeingPair(values = [8,1,5,2,6])) # i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11