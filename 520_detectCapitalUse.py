def detectCapitalUse(word):
    if word[0] == word[0].upper() and word[1] != word[1].upper():
        for i in range(2, len(word)):
            if word[i] == word[i].upper():
                return False
    if word[0] == word[0].upper() and word[1] == word[1].upper():
        for i in range(2, len(word)):
            if word[i] != word[i].upper():
                return False
    if word[0] == word[0].lower() and word[1] == word[1].lower():
        for i in range(2, len(word)):
            if word[i] != word[i].lower():
                return False
    if word[0] == word[0].lower() and word[1] != word[1].lower():
        return False
    return True
print(len("gaqrzczpmtsxlwxdacitrcgklziiya"))
# print(detectCapitalUse("USA"))
# print(detectCapitalUse("FlaG"))
# print(detectCapitalUse("Leetcode"))
# print(detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"))