# Given the string representations of two integers,
# return the string representation of the sum of those integers.
#
# For example:
#
# sumStrings('1','2') // => '3'
# A string representation of an integer will
# contain no characters besides the ten numerals "0" to "9".

def sum_strings(x, y):
    return str(int(x) + int(y))

print(sum_strings("1", "2"))