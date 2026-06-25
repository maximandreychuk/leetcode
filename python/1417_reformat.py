def reformat(s: str):
    result = ""
    alpha, digits = [], []
    for i in s:
        if i.isalpha():
            alpha.append(i)
        else:
            digits.append(i)
    if abs(len(alpha) - len(digits)) > 1:
        return ""
    if len(digits) == len(alpha):
        i = 0
        while i < len(alpha):
            result += f"{digits[i]}{alpha[i]}"
            i += 1
        return result
    if len(digits) > len(alpha):
        i = 0
        while i < len(alpha):
            result += f"{digits[i]}{alpha[i]}"
            i += 1
        result += digits[-1]
    else:
        i = 0
        while i < len(digits):
            result += f"{alpha[i]}{digits[i]}"
            i += 1
        result += alpha[-1]
    return result


print(reformat(s = "a0b1c22")) # 2a0b1c2
