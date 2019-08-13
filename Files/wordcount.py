import sys

inF = sys.argv[1]
outF = sys.argv[2]

inFile = open(inF, "r")
outFile = open(outF, "w")

line = inFile.readline()

flag = True

while(line):
    if flag:
        inFile.seek(0)

    line = inFile.readline()
        

