# Complete the function scramble(str1, str2) that returns true
# if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.

# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


def scramble(s1, s2):
    counter = 0
    for i in s2:
        if i in s1:
            counter += 1
    if counter == len(s2):
        return True
    else: return False

print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))

