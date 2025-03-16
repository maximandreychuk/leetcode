from collections import Counter


def maxNumberOfBalloons(text):
    txt = Counter(text)
    tmp = "balloon"
    l = len(tmp)
    # tmp = Counter("balloon")
    cnt = 0
    while l > 0:
        nl = 0
        for k in txt.keys():
            if k in tmp:
                if txt[k] < 0:
                    return cnt
                nl += 1
                txt[k] -= 1
        print(nl)
        if l == nl:
            cnt += 1
        else:
            return cnt


print(maxNumberOfBalloons(text="loonbalxballpoon"))
