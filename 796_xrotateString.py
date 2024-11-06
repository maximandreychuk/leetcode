def rotateString(s, goal):
    shift = 0
    while shift < len(s):
        s = s[1:] + s[0]
        if s == goal:
            return True
        shift += 1
    return False


print(rotateString(s = "12345", goal = "51234"))
print(rotateString(s = "abcde", goal = "cdeab"))
print(rotateString(s = "abcde", goal = "abced"))