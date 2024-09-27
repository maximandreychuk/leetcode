# Complete the solution so that the function will
# break up camel casing, using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    lst=[i for i in s]
    step = 0
    for idx in range(len(s.upper())):
        if s[idx] == s.upper()[idx]:
            lst.insert(idx+step," ")
            step+=1
    return "".join(lst)



print(solution("camelCasingTestNone"))