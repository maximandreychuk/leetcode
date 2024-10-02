# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
#
# Here's the deal:
#
# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
from pydoc import replace


# " Hello there thanks for trying my Kata "  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false

def generate_hashtag(s):
    if len(s) > 140 or s == "" or s == " ":
        return False
    det = [[j for j in i] for i in s.replace(" ", " ").split()]
    det = [[letter.lower() for letter in word] for word in det]
    for i in det:
        i[0] = i[0].upper()
    res = ["".join(i) for i in det]
    tag = "#"
    for i in res:
        tag+=i
    if len(tag) > 140:
        return False
    else:
        return tag

print(generate_hashtag("    Hello   there thanks for trying my Kata ")) #HelloThereThanksForTryingMyKata
print(generate_hashtag("CoDeWaRs is niCe")) #CodewarsIsNice