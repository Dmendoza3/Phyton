import time

def printTable(t):
    for i in range(0, len(t)):
        print(" _", end = "")
    print("")
    for i in t:
        print("|", end="")
        for j in i:
            if j == 0 :
                print("_", end = "|")
            else:
                print("*", end = "|")
        print()

class Snake:
    def __init__(self, nwX = 0, nwY = 0, pwr = 1, direction = 1):
        self.x = nwX
        self.y = nwY
        self.tail = pwr * [0]
        self.pwr = pwr
        self.dir = direction #1 = up, 2 = down, 3 = left, 4 = right
        for i in range(0, pwr):
            self.tail[i] = 0
    
    def move(self):
        self.tail[0] = self.dir
        for i in range(1, len(self.tail) - 1):
            self.tail[i] = self.tail[i - 1]
        if(self.dir == 1):
            self.y = self.y - 1
        if(self.dir == 2):
            self.y = self.y + 1
        if(self.dir == 3):
            self.x = self.x - 1
        if(self.dir == 4):
            self.x = self.x + 1

def drawSnake(snake, t):
    t[snake.x][snake.y] = snake.dir
    for i in snake.tail:
        if(i == 0):
            pass
        if(i == 1):
            t[snake.x][snake.y - 1] = i 
        if(i == 2):
            t[snake.x][snake.y + 1] = i 
        if(i == 3):
            t[snake.x - 1][snake.y] = i
        if(i == 4):
            t[snake.x + 1][snake.y - 1] = i
    snake.move()
    

def mainGame(iniX, iniY, t):
    snk = Snake(iniX, iniY, 3)
    while True:
        drawSnake(snk, t)
        printTable(table) 
        time.sleep(2)

width = 8
height = 8
table = width * [height * [0]]

mainGame(4, 4, table)
