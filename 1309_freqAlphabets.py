from string import ascii_letters

def freqAlphabets(s):
    idx_letter_dict = {}
    for i in range(len(ascii_letters)):
        idx_letter_dict[str(i + 1)] = ascii_letters[i]

    res = ''
    i = len(s) - 1

    while i >= 0:
        if s[i] == '#':
            res += idx_letter_dict[s[i - 2:i]]
            i -= 3
        else:
            res += idx_letter_dict[s[i]]
            i -= 1
    return res[::-1]


print(freqAlphabets(s = "10#11#12"))
#done