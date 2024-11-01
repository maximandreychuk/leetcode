def countSegments(s):
    start = 0
    for char in s.split():
        if char != " ":
            start += 1
    return start



print(countSegments("Hello,   my name is John"))
print(countSegments("       "))
print(countSegments(" "))