def stringMatching(words):
    i, res = 0, []
    while i < len(words):
        for j in range(len(words)):
            if words[i] in words[j] and i != j and words[i] not in res:
                res.append(words[i])
        i += 1
    return res




print(stringMatching(words = ["mass","as","hero","superhero"])) # ["as","hero"]

