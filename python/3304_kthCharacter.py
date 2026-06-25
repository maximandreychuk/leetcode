def kthCharacter(k):
    from string import ascii_lowercase as letters
    word = letters[0]
    while len(word) < k:
        new_word = ''.join([letters[letters.find(char)+1] for char in word])
        word += new_word
    return word[k-1]

print(kthCharacter(5))
#done
