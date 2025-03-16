def countCharacters(words, chars):
    chars_count_dict = {}
    for i in chars:
        chars_count_dict.setdefault(i, 0)
        chars_count_dict[i] += 1
    result = 0
    for word in words:
        copy = chars_count_dict
        adding = 0
        for c in word:
            if copy.get(c) is not None and copy.get(c) != 0:
                copy[c] -= 1
                adding += 1
            else:
                break
        chars_count_dict = copy
        result += adding
    return result






print(countCharacters(words = ["cat", "bt", "hat", "tree"], chars = "atach"))
# Example
# 1:
#
# Input: words = ["cat", "bt", "hat", "tree"], chars = "atach"
# Output: 6
# Explanation: The
# strings
# that
# can
# be
# formed
# are
# "cat" and "hat"
# so
# the
# answer is 3 + 3 = 6.
# Example
# 2:
#
# Input: words = ["hello", "world", "leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The
# strings
# that
# can
# be
# formed
# are
# "hello" and "world"
# so
# the
# answer is 5 + 5 = 10.