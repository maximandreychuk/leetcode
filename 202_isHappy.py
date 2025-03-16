class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        new_n = 0
        for i in range(len([int(i) for i in str(n)] )):
            new_n += [int(i) for i in str(n)][i]*[int(i) for i in str(n)][i]
        try:
            return Solution.isHappy(self, n=new_n)
        except RecursionError:
            return False


s = Solution()
print(s.isHappy(1)) # true
print(s.isHappy(11)) # false
print(s.isHappy(19)) # true
print(s.isHappy(20)) # false
print(s.isHappy(14)) # 