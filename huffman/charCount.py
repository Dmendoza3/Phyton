def characterCount(string):
    charDict = {}
    for x in string:
        if charDict.get(x):
            charDict[x] = charDict[x] + 1
        else:
            charDict[x] = 1
    return charDict