def printGraph(start):
    if gr[start]:
        print(gr[start])
        for x in gr[start]:
            printGraph(x)
gr = {}

gr['a'] = ['b']
gr['b'] = ['c', 'd']
gr['c'] = ['e', 'f', 'g']
gr['d'] = ['f', 'g']

printGraph('a')