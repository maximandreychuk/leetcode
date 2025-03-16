def hasSpecialSubstring( s: str, k: int) -> bool:
        for i in range(len(s)-k):
            char = s[i]
            cnt = len(s[i:k])
            for c in s[i:k]:
                if c == char:
                    cnt -= 1
            if cnt == 0:
                return True
        return False

print(hasSpecialSubstring( s = "aaabaaa", k = 3))
#partial