# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.


def find_short(s):
    lst = [i for i in s.split(" ")]
    l = len(s)
    for i in lst:
        if len(i)<l:
            l = len(i)
    return l

print(find_short("bitcoin take over the world maybe who knows perhaps"))