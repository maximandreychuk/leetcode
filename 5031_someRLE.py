def base_rle(string):
    i = 1
    new_str = ''
    while i < len(string) - 1:
        try:
            numb = int(string[i-1])
            add = numb*string[i]
            new_str += add
        except ValueError:
            pass
        i += 1
    try:
        numb = int(string[-2])
        add = numb*string[-1]
        new_str += add
    except ValueError:
        new_str += string[-1]
    return new_str

print(base_rle("4A3B2C1D2A")) #AAAABBBCCDAA