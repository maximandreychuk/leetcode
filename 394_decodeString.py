def decodeString(s: str) -> str:
    result = ''
    for i in range(len(s)):
        if s[i] == '[':
            l = r = i
            while s[r] != ']':
                r += 1
            result += int(s[i-1])*f'{s[l+1:r]}'
            i += r - l
    return result

print(decodeString(s = "3[a]2[bc]"))


# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# со вложенностью посложнее
# Input: s = "3[a2[c]]"
# Output: "accaccacc"