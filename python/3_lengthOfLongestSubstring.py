def lengthOfLongestSubstring(s):
    result = potential = s[0]
    for i in range(1, len(s)):
        if s[i] not in potential:
            potential += s[i]
        else:
            if len(potential) > len(result):
                result = potential
            potential = s[i]
    if len(potential) > len(result):
        result = potential
    return len(result)


print(lengthOfLongestSubstring("abcabcdbb"))
print(lengthOfLongestSubstring(s = "pwwkew"))
print(lengthOfLongestSubstring(s = "bbbbbb"))