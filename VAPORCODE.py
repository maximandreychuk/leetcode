# ASC Week 1 Challenge 4 (Medium #1)
#
# Write a function that converts any sentence into a V A P O R W A V E sentence.
# a V A P O R W A V E sentence converts all the letters into uppercase,
# and adds 2 spaces between each letter (or special character) to create this V A P O R W A V E effect.
#
# Note that spaces should be ignored in this case.
#
# Examples
# "Lets go to the movies"       -->  "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"
# "Why isn't my code working?"  -->  "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"

def vaporcode(s):
    new_s = ""
    for idx in range(1,len(s)-1):
        if s[idx] != " ":
            new_s += f" {s[idx].upper()} "
    if s[0] != " ":
        new_s = s[0].upper() + " " + new_s
    if s[-1] != " ":
        new_s = new_s + " " + s[-1].upper()
    return new_s

print(vaporcode("Lets go to the movies"))