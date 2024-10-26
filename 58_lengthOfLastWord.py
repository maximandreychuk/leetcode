def lengthOfLastWord(s):
    s = s[::-1]
    lst = s.split(" ")
    for i in lst:
        if i != "":
            return len(i)





print(lengthOfLastWord("   fly me   to   the moon  "))
# print(lengthOfLastWord("luffy is still joyboy"))