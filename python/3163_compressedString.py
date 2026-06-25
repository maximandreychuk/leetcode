def compressedString(word):
    if len(word) == 1:
        return f'1{word[0]}'
    if len(word) == 2:
        if word[0] == word[1]:
            return f'2{word[0]}'
        else:
            return f'1{word[0]}1{word[1]}'
    cnt = 1
    comp = ""
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            if cnt == 9:
                comp += f'{cnt}{word[i]}'
                cnt = 1
            else:
                cnt += 1
        else:
            comp += f'{cnt}{word[i - 1]}'
            cnt = 1
    if word[-1] == word[-2]:
        comp += f'{cnt}{word[-1]}'
    else:
        comp += f'1{word[-1]}'
    return comp


print(compressedString(word = "aaaaaaaaaaaaaabbc")) #"9a5a2b"
#done
