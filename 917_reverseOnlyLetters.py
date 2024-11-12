from string import ascii_letters as asc

def reverseOnlyLetters(s):
    s = [str(i) for i in s]
    left, right = 0, len(s)-1
    while left < right:
        if s[left] not in asc:
            left += 1
        elif s[right] not in asc:
            right -= 1
        else:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    return "".join(s)



print(reverseOnlyLetters(s = "a-bC-dEf-ghIj")) #"j-Ih-gfE-dCba"
print(reverseOnlyLetters(s = "Test1ng-Leet=code-Q!")) # "Qedo1ct-eeLg=ntse-T!"