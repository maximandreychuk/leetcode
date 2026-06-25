def licenseKeyFormatting(s, k):
    result = ""
    s = list(reversed(s))
    for i in range(len(s)):
        detail = ""
        while len(detail) < k:
            if s[i] != "-":
                detail+=s[i]
                i+=1
        result += f"{detail}-"








print(licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4)) # "5F3Z-2E9W"
print(licenseKeyFormatting(s = "2-5g-3-J", k = 2)) # "2-5G-3J"