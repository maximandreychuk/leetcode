def buddyStrings(s, goal):
    i = 0
    s, goal = [i for i in s], [i for i in goal]
    while i < len(goal)//2:
        for j in range(i+1, len(s)):
            s[i], s[j] = s[j], s[i]
            if s == goal:
                return True
            else:
                s[i], s[j] = s[j], s[i]
        i += 1
    return False

print(buddyStrings("abab", "abab")) # t
