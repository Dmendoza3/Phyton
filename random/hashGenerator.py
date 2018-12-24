def genHash(inData, primeNum = 73):
    pieces = [0,0,0,0]

    if type(inData) == str:
        for x in inData:
            pass
    elif type(inData) == int:
        pieces[0] = (inData % primeNum) % 256
        pieces[1] = (pieces[0] % inData) % 256
        pieces[2] = (inData + (primeNum % 16)) % 256
        pieces[3] = (pieces[0] + pieces[1] + pieces[2]) % 256
    elif type(inData) == float:
        decimalPart = int(inData)
        floatingPart = inData - decimalPart

    hashed = ""
    for x in pieces:
        hashed = hashed + hex(x)[2:]

    return hashed



print(genHash(1234))
print(genHash(12))

