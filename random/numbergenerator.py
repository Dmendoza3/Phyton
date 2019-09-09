def generate(grf, n = 1, ini = 0):
    gen = ""
    sel = ini
    for x in range(n):
        for y in range(x):
            sel = grf[sel]
        gen = str(sel) + gen
    return gen
graph = [5,1,2,4,3,7,8,6,9,0]

print(generate(graph, 10, 0))
