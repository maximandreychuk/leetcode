def commonChars(words):
    cnt = i = 1
    res = []
    for char in words[0]:
        while i < len(words):
            if char in words[i]:
                cnt += 1
            i += 1
        if cnt == len(words):
            res.append(char)
        cnt = i = 1
    return res




print(commonChars(words = ["bella","label","roller"]))
print(commonChars(["cool","lock","cook"]))