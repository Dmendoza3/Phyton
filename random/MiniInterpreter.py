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


def preprocess(name = 'default.mini'):
    miniF = open(name, 'r')
    preproStr = ""
    line = ' '
    while line:
        line = miniF.readline()
        truncLine = truncate(line)
        preproStr = preproStr + truncLine
    
    miniF.close()
    return preproStr

def tokenizer(tokens = ""):
    pass

print(preprocess("code.mini"))
