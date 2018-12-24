def newFile(name = 'default.txt', fields = {'default':('str', 20)}):
    types = {'str' : 1, 'sint' : 2, 'uint' : 3, 'double' : 4, }
    if name == '':
        return False
    else:
        newF = open(name, 'w')
        metadata = ''
        for x in fields:
            metadata = metadata + x + fields[x][0]