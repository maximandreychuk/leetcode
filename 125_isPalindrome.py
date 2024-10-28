
def isPalindrome(s: str) -> bool:
    spec = (" ", "", ":", ",", ";", ".")
    s1 = [i for i in s.lower() if i.isalnum()]
    s2 = list(reversed(s1))
    return s1 == s2


print(isPalindrome("A man, a plan, a canal: Panama"))