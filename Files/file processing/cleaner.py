import sys

if len(sys.argv) < 2:
    print("Faltan parametros.")
    exit()

inFile = open(sys.argv[1])
outFile = open("cleaned.txt" if len(sys.argv) < 3 else sys.argv[2], "w")

line = " "
while(line):
    line = inFile.read()
    newline = ""
    for x in line:
        if ord(x) > 0 and ord(x) < 255:
            newline = newline + x
    outFile.write(newline)

inFile.close()
outFile.close()