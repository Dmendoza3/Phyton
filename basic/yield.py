def arrayYield():
    arr = [9,8,7,6,5,4,3,2,1]
    for x in arr:
        yield x

for x in arrayYield():
    print(x)