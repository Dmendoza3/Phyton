import math

ofile = open("circle.txt", "w")

def printGrid():
    for x in grid:
        print("[", end="", file=ofile)
        for y in x:
            print(y, end=", ", file=ofile)
        print("]", file=ofile)

w = 20
h = 20
grid = [[" " for x in range(w)] for y in range(h)] 

origin = (10, 10)

radius = 5

for ang in range(0, 360):
    angr = math.radians(ang)
    for rad in range(radius):
        newx = math.trunc(rad * math.sin(angr))
        newy = math.trunc(rad * math.cos(angr))

        #if(ang >= 90 and ang <= 180):
        #print(ang, origin[0] + newx, origin[1] + newy)
        grid[origin[0] + newx][origin[1] + newy] = "*"

grid[origin[0]][origin[1]] = "x"

printGrid()