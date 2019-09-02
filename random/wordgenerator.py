def baseN(x, n=36):
    alphabase = [x for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    res = ""
    while x:
        res = alphabase[x % n] + res
        x = int(x / n)
    return res if res else "0"

outFile = open("wordgen.txt","w")
strlen = 5
for x in range(0, 36 ** strlen):
    print(baseN(x),file=outFile)

outFile.close()