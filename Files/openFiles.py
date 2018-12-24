outF = "./GenList.txt"

outFile = open(outF, "r")

line = " "
while(line):
    line = outFile.readline()
    print(line)

outFile.close()