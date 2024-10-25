def isValid(st):
    staples = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    if len(st) <= 1: return False
    stack = []
    for i in st:
        if i in staples.values():
            stack.append(i)
        elif i in staples.keys():
            if not stack or stack[-1] != staples[i]:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True


print(isValid("(]"))
print(isValid("()[]{}"))
print(isValid("([])"))