class base:
    def __init__(self,x):
        self.x = x

class a(base):
    def __init__(self,x,y):
        super().__init__(x)
        self.y = y

    def sup(self):
        return super()

class b(a):
    def __init__(self, x, y ,z):
        super().__init__(x,y)
        print(super().super())
        self.z = z

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)

x = 2
print(1 | 2)
if x == 1 | 2:
    print("coor", "no coor")