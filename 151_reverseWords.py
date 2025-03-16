def reverseWords(s):
    words = []
    start = 0
    for i in range(len(s)):
        if s[i] == " ":
            if i > start:  # Check if a word exists before the space
                words.append(s[start:i])
            start = i + 1  # Update start for the next word
    if len(s) > start:  # Handle trailing word
        words.append(s[start:])

    return " ".join(reversed(words))



print(reverseWords(s = "the sky is blue")) # "blue is sky the"


