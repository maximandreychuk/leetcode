def reverseWords(s):
    new_s = ""
    start = end = 0
    for i in range(len(s)):
        if s[i] != " ":
            end += 1
        else:
            new_s += s[start:end][::-1]
            start = i
            end = i + 1
            new_s += s[i]
    new_s += s[start:end][::-1]

    return len(new_s), new_s



print(len("s'teL ekat  edoCteeL tsetnoc "))

print(reverseWords("s'teL ekat  edoCteeL tsetnoc ")) # "s'teL ekat edoCteeL tsetnoc "