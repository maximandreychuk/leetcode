def longest_palindrome(s):
    longest = ''
    for i in range(len(s)):
        to_right = s[i:]
        if to_right == to_right[::-1] and len(to_right) > len(longest):
            longest = to_right
        to_left = s[::-1][i:]
        if to_left == to_left[::-1] and len(to_left) > len(longest):
            longest = to_left
    return longest


print(longest_palindrome('ffffffvvgvvvvv'))

