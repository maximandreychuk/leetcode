from string import ascii_uppercase as asc

def titleToNumber(columnTitle):
    icnt = 0
    for i in columnTitle[::-1]:
        jcnt = 1
        for j in asc:
            if j == i:
                icnt += len(asc[:jcnt])
            else:
                jcnt += 1
    return icnt


print(titleToNumber("ZY")) #701