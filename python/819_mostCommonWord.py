from string import ascii_letters

def mostCommonWord(paragraph, banned):
    all_words = []
    start, end = 0, 0
    for i in range(len(paragraph)):
        if paragraph[i] in ascii_letters:
            end += 1
        else:
            if paragraph[start:end+1][0] == " ":
                all_words.append(paragraph[start+1:end+1].lower())
            else:
                all_words.append(paragraph[start:end + 1].lower())
            start = end = i
    all_words.append(paragraph[start+1:end].lower())
    dct = {}
    for i in all_words:
        if len(i) > 1:
            if i not in dct.keys():
                dct[i] = 1
            else:
                dct[i] += 1
        else:
            if i not in dct.keys() and i in ascii_letters:
                dct[i] = 1
            elif i in dct.keys() and i in ascii_letters:
                dct[i] += 1
    result = ""
    numb = 0
    for i in dct.keys():
        if len(banned) > 0:
            if dct[i] > numb and dct[i] < dct[banned[0]]:
                numb = dct[i]
                result = i
        else:
            if dct[i] > numb:
                numb = dct[i]
                result = i
    return result



print(mostCommonWord(paragraph = "a.", banned = []))
print(mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"])) # ball