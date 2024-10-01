# We want to create a function that will
# add numbers together when called in succession.
#
# add(1)(2) # equals 3

class add(int):
    def __call__(self,n):
        return add(self + n)

print(add(1)(2)) # 3