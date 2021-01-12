def remove(line):
    notWanted = ["is", "the", "and", "of", "to", "a", "or", "for", "in", "at", "than", "an", "but", "do", "ah", "oh"
    "so", "if", "its", "her", "aren't", "isn't"]

    line = " " + line
    for word in notWanted:
        spaced = " " + word + " "
        line = line.replace(spaced, " ")

    return line[1:]

inPath = './randomtext.txt'
outPath = './removedWords.txt'

inFile = open(inPath, 'r')
outFile = open(outPath, 'x')

cnt = 0

while True:
    line = inFile.readline()

    if not line:
        break

    line = remove(line.lower())
    cnt = cnt + len(line)
    print("Processed", (cnt / 1024) / 1024,"MB")
    outFile.write(line)
    
print("End of file")