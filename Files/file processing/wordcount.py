import sys

inF = sys.argv[1]
outF = sys.argv[2] if len(sys.argv) > 2 else "counted.csv"
sep = " "#sys.argv[3] if 

inFile = open(inF, "r")
outFile = open(outF, "w")

line = inFile.readline()

flag = True

wordCount = {}

while(line):
    if flag:
        inFile.seek(0)
        flag = False

    line = inFile.readline()
    #lineArr = line.strip().split(sep)
    lineArr = line.split()
    for word in lineArr:
        if wordCount.get(word.lower(), -1) != -1:
            wordCount[word.lower()] =  wordCount[word.lower()] + 1
        else:
            wordCount[word.lower()] = 1

print("word;count", file=outFile)
for word in wordCount:
    print(word + ";" + str(wordCount[word]), file=outFile)

    
        

