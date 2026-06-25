def longestPalindrome(s):
    result = []
    for i in range(len(s)):
        mem = s[i:]
        start = 1
        while start < len(mem):
            char = mem[start:]+mem[:start]
            if char == char[::-1]:
                result.append(char)
            start+=1
    return max([len(i) for i in result])


from itertools import product

def foo(s):
    yield product(*([s]*len(s)))

for i in foo("abc"):
    print(list(i))



# print(foo("abccccdd"))
# print(longestPalindrome("abccccdd")) #"dccaccd"7