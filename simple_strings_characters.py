# In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.
#
# Solve("*'&ABCDabcde12345") = [4,5,5,3].
# --the order is: uppercase letters, lowercase, numbers and special characters.
# More examples in the test cases.
#
# Good luck!


def solve(s: str):
    result = [0 for _ in range(0,4)]
    for i in s:
        try:
            2 * int(i)
            result[2] += 1
        except ValueError:
           if i.upper() == i.lower():
               result[3] += 1
           elif i.isupper():
               result[0] += 1
           elif i.islower():
               result[1] += 1
    return result


solve("*'&ABCDabcde12345")