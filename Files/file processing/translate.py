def translate(line):
    toSearch = ["<br />", "&gt;"]

    toTranslate = ["\n", ">"]

    for i, word in enumerate(toSearch):
        line = line.replace(word, toTranslate[i])

    return line

inPath = './rawtext.txt'
outPath = './translatedWords.txt'

inFile = open(inPath, 'r')
outFile = open(outPath, 'x')

cnt = 0


while True:
    line = inFile.readline()

    if not line:
        break

    line = translate(line.lower())
    cnt = cnt + len(line)
    print("Processed", (cnt / 1024) / 1024,"MB")
    outFile.write(line)
    
print("End of file")