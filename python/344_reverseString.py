def reverseString(s):
    j = -1
    for i in range(len(s)//2):
        s[i], s[j] = s[j], s[i]
        j-=1
    return s



print(reverseString(["h","e","l","l","o"])) # ["o","l","l","e","h"]