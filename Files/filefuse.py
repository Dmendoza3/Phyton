import sys

inF1 = sys.argv[1]
inF2 = sys.argv[2]

if len(sys.argv) == 4: 
    outF = sys.argv[3]
else:
    outF = "./outFile.txt"

inFile1 = open(inF1, "r")
inFile2 = open(inF2, "r")
outFile = open(outF, "w")

line1 = inFile1.read(1)
line2 = inFile2.read(1)

flag = True
while(line1 or line2):
    if flag:
        inFile1.seek(0)
        inFile2.seek(0)

    line1 = inFile1.read(1)
    line2 = inFile2.read(1)

    if len(line1) > 1:
        line1 = chr()
    if len(line2) > 1:
        line2 = chr(0)

    #change this
    chr1 = ord(line1[0]) #if line1 == chr(0) else 0
    chr2 = ord(line2[0]) #if line2 == chr(0) else 0

    linexor = chr1 ^ chr2
    outFile.write(chr(linexor))
