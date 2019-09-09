def getNumber(st):
    c = 0
    con = ""
    if len(st) <= 2:
        return 0
    while True:
        c = c - 1
        if st[c] != ' ' :
            con = st[c] + con
        else :
            break
    return float(con)

a = ["12","34","56"]
str_ = "zfsdf3d4ssdf5d6"

#if any(x in str_ for x in a):

print(["asd","2323","34re"])