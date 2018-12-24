def truncate(oldStr = ''):
    oldStr = oldStr.replace('\t', ' ')

    listSplit = oldStr.split(' ')

    while True:
        try:
            listSplit.remove('')
        except:
            break

    newStr = ""
    for x in listSplit:
        newStr = newStr + x + " "

    return newStr[:len(newStr) - 1]

st = "  \t  aasa   das  das d \t"
truncStr = truncate(st)

print(len(st),len(truncStr))
print(st, truncStr, sep = "\n")