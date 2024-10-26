def strStr(haystack, needle):
    for i in range(len(haystack)):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                return i
    return -1




# print(strStr(haystack = "sadbutsad", needle = "sad"))
# print(strStr("leetcode", "leeto"))
print(strStr("hello", "ll"))

