def isLongPressedName(name, typed):
    new_name = ""
    b = a = 0
    while b < len(typed):
        if typed[b] != name[a]:
            b += 1
        else:
            new_name += typed[b]
            a += 1
            b += 1
    return name == new_name


print(isLongPressedName(name = "alex", typed = "aaleex"))
print(isLongPressedName(name = "saeed", typed = "ssaaedd"))