# The goal of this exercise is to convert a string to a new string where each character
# in the new string is "(" if that character appears only once
# in the original string, or ")" if that character appears more than once
# in the original string. Ignore capitalization when determining
# if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("

from collections import defaultdict


def duplicate_encode(word):
    word = [i for i in word.lower()]
    letter_amount_dict=defaultdict(int)
    for i in word:
        letter_amount_dict[i]+=1
    for idx in range(0,len(word)):
        if letter_amount_dict[word[idx]] != 1:
            word[idx]=")"
        else:
            word[idx] = "("
    result = "".join(word)
    return result









print(duplicate_encode("Success"))