def validWord(word, abbr):
    start = end = 0
    res = ""
    start = 0
    for i in range(len(abbr)):
        if i != int(i):
            start = end = i
        else:










print(validWord(word="internationalization", abbr = "i12iz4n"))