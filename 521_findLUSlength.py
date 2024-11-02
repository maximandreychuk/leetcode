def findLUSlength(a, b):
    if a != b:
        if len(a) < len(b):
            return len(b)
        else:
            return len(a)
    return -1

print(findLUSlength("swoegxvzsfetrdtnoucawucug", "gaqrzczpmtsxlwxdacitrcgklziiya"))