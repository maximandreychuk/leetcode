def backspaceCompare(s, t):
    i = 0
    new_s = new_t = ""
    while i < len(s) or i < len(t):
        if i < len(s):
            if s[i] != "#":
                new_s += s[i]
            else:
                new_s = new_s[:len(new_s)-1]
        if i < len(t):
            if t[i] != "#":
                new_t += t[i]
            else:
                new_t = new_t[:len(new_t)-1]
        i += 1
    return new_s == new_t


print(backspaceCompare(s = "ab#c", t = "ad#c"))
print(backspaceCompare(s = "ab##", t = "c#d#"))
print((backspaceCompare(s = "a#c", t = "b")))