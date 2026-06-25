from string import ascii_uppercase as asc

def convertToTitle(columnNumber):
    title = ""
    while columnNumber > 0:
        title += asc[columnNumber % 26-1]
        columnNumber //= 26
    return title[::-1]


print(convertToTitle(53))
print(convertToTitle(2147483647))