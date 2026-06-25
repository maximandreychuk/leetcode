from curses.ascii import isspace
from string import ascii_letters as asc

def toGoatLatin(sentence):
    cur_word = res = ""
    temp = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    cnt = 1
    for i in range(len(sentence)):
        if sentence[i].isspace():
            if cur_word:
                if cur_word[0] in temp:
                    cur_word = cur_word + "ma" + ("a" * cnt)
                    res += cur_word + " "
                    cnt += 1
                else:
                    cur_word = cur_word + cur_word[0] + "ma" + ("a" * cnt)
                    cur_word = cur_word[1:]
                    res += cur_word + " "
                    cnt += 1
            cur_word = ""
        else:
            cur_word += sentence[i]
    if cur_word:
        if cur_word[0] in temp:
            cur_word = cur_word + "ma" + ("a" * cnt)
            res += cur_word
        else:
            cur_word = cur_word + cur_word[0] + "ma" + ("a" * cnt)
            cur_word = cur_word[1:]
            res += cur_word
    return res


print(toGoatLatin(sentence = "I speak Goat Latin")) # "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"


