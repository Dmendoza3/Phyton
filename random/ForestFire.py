from random import randrange
import time

def printPlain(p = [[0]], w = 1, h = 1):
    for i in range(w):
        for j in range(h):
            if p[i][j] > 0:
                print('T', end = ' ')
            elif p[i][j] < 0:
                print('M', end = ' ')
            else:
                print('.', end = ' ')
        print()

    print('_' * 20)

def passTime(p = [[0]], w = 1, h = 1, treeInitProb = 10, treeProbGain = 10,treeFireInit = 1, treeFireGain = 5):
    treeProb = treeInitProb
    for i in range(w):
        for j in range(h):
            if (treeProb <= randrange(100)) and (p[i][j] == 0):
                treeProb += treeProbGain
            else:
                treeProb = treeInitProb
                p[i][j] = treeFireInit

            if p[i][j] < randrange(100):
                p[i][j] += treeFireGain
            else:
                p[i][j] = -10

            if p[i][j] < 0:
                p[i][j] += 1
            printPlain(p, w, h)
            time.sleep(2)


w = 10
h = 10
plain = [[0]*h]*w
passTime(plain, w, h)
printPlain(plain, w, h)
