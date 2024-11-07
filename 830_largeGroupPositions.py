def largeGroupPositions(s):
    tail, head, result = 0, 1, []

    while head < len(s):
        if s[head] != s[tail]:
            if head - tail >= 3:
                result.append([tail,head-1])
            tail = head
        else:
            head += 1
    if head - tail >= 3:
        result.append([tail,head-1])
    return result




print(largeGroupPositions("abbxxxxzzy")) # [[3,6]]
print(largeGroupPositions(s = "abcdddeeeeaabbbcd")) # [[3,5],[6,9],[12,14]]