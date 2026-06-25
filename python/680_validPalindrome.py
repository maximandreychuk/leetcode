def validPalindrome(s):
    for i in range(1, len(s)):
        p = s[:i-1] + s[i:]
        if p == p[::-1]:
            return True
    return True if s[:len(s)-1] == s[:len(s)-1][::-1] else False




print(validPalindrome("abca"))
print(validPalindrome("abc"))
print(validPalindrome("eccer"))

