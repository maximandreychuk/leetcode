def getEncryptedString(s,k):
    new_str = ''
    for i in range(len(s)):
        new_idx = (i+k) % len(s)
        new_str += s[new_idx]
    return new_str


print(getEncryptedString(s = "byd", k = 4)) #tdar
#done