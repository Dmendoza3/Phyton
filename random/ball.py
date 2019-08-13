import time

class ball():
    def __init__(self, x = 5, y = 5, sx = 1, sy = 1, sp = 2, w = 10, h = 10):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.sp = sp
        self.w = w
        self.h = h

    def move(self):
        self.x = self.x + self.sx * self.sp
        self.y = self.y + self.sy * self.sp


        if(self.x < 0):
            self.x = 0
            self.bounce(False)

        if(self.y < 0):
            self.y = 0
            self.bounce(True)

        if(self.x > self.w):
            self.x = self.w
            self.bounce(False)
        
        if(self.y > self.h):
            self.y = self.h
            self.bounce(True)

    def bounce(self, ver):
        if not ver:
            if(self.sx > 0):
                sx = -1
            else:
                sx = 1
        else:
            if(self.sy > 0):
                sy = -1
            else:
                sy = 1

    def printBall(self):
        for w in range(0, self.w):
            for h in range(0, self.h):
                if(self.x == w and self.y == h):
                    print("*", end = "")
                else:
                    print("_", end = "")
            print()

b = ball()
while True:
    b.move()
    b.printBall()
    time.sleep(0.5)
    

