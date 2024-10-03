# Move every letter in the provided string forward 10 letters through the alphabet.
#
# If it goes past 'z', start again at 'a'.
#
# Input will be a string with length > 0.
import string


def move_ten(st):
    new_st = ""
    st = [i for i in st]
    db = string.ascii_lowercase + string.ascii_lowercase
    for let in st:
        if let in db:
            new_idx = db.index(let) + 10
            new_st += db[new_idx]

    return new_st

print(move_ten("zsfsv"))