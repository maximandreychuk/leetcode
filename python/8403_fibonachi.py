def fibonacci_iterative(n):
    a = 0
    b = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci_iterative(11))

class Obj:
    def __init__(self, value):
        self.value = value


obj1 = Obj(2)
obj2 = Obj(2)
counter = {obj2: '2'}
for i in counter:
    print(hash(i))

obj2 = Obj(1)
counter = {obj2: '2'}
for i in counter:
    print(hash(i))

