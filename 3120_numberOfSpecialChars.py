from black.linegen import partial


def numberOfSpecialChars(word):
    letter_lowercase_uppercase_dict = {}
    cnt = 0
    for i in word:
        if i.isupper() and i.lower() in letter_lowercase_uppercase_dict.keys():
            if letter_lowercase_uppercase_dict[i.lower()] != 2:
                letter_lowercase_uppercase_dict[i.lower()] = 2
                cnt += 1
        elif i.islower() and i.lower() not in letter_lowercase_uppercase_dict.keys():
            letter_lowercase_uppercase_dict.setdefault(i, 1)
    return letter_lowercase_uppercase_dict, cnt

print(numberOfSpecialChars(word = "abBCab"))
#partial