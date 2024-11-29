def isPrefixOfWord(sentence, searchWord):
    cnt = 1
    current_word = ""
    for char in sentence:
        if char != " ":
            current_word += char
        else:
            if current_word:
                if searchWord == current_word[0:len(searchWord)]:
                    return cnt
                current_word = ""
                cnt += 1
    if current_word:
        if searchWord == current_word[0:len(searchWord)]:
            return cnt
    return -1


print(isPrefixOfWord(sentence = "  i love eating burger", searchWord = "burg")) # 4
