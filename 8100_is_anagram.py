def is_anagram(s,t):
    return sorted(s) == sorted(t)


print(is_anagram(s = "anagram", t = "nagaram"))