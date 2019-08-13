class test:
    def __init__(self):
        self.i = 0
        self.t = 0

class A:
    def __init__(self,x = 5):
        self.x = x

class B(A):
    def __init__(self, x = 5, y = 5):
        super().__init__(x)
        self.y = y

x = B(10,20)


print(x.x)