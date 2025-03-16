def base_rle(string):
    cnt = 1
    new_str = ''
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            cnt += 1
        else:
            if cnt == 1:
                new_str += f'{string[i-1]}'
            else:
                new_str += f'{cnt}{string[i - 1]}'
            cnt = 1
    new_str += f'{cnt}{string[-1]}'
    return new_str


print(base_rle('AAAABBBCCDAA')) # 4A3B2CD2A
