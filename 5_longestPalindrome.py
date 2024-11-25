def longestPalindrome(s):
    long_palindrom = ""
    tail = 0
    while tail < len(s):
        for i in range(tail, len(s)):
            if s[tail:i] == s[tail:i][::-1]:
                if len(s[tail:i]) > len(long_palindrom):
                    long_palindrom = s[tail:i]
        tail += 1
    return long_palindrom




print(longestPalindrome(s = "cbbd")) # bab