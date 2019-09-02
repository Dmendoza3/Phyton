import random

random.seed()

outF = "./GenList.txt"

outFile = open(outF, "w")

for i in range(1,10000):
    outFile.write(str(random.randint(0,100)) + ",")

