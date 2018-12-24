def checkValid(arr, val):
    count = 0
    for i in range(0, 9):
        if(arr[i] == val):
            count = count + 1

    return (count == 1)


def getCol(mat, index):
    col = []
    for i in range(0, 9):
        col.append(mat[i][index])
    return col

def getGroup(mat, row, col):
    group = []
    row = row - (row % 3)
    col = col - (col % 3)
    
    group.append(mat[row    ][col    ])
    group.append(mat[row + 1][col    ])
    group.append(mat[row    ][col + 1])
    group.append(mat[row + 2][col    ])
    group.append(mat[row    ][col + 2])
    group.append(mat[row + 1][col + 1])
    group.append(mat[row + 1][col + 2])
    group.append(mat[row + 2][col + 1])
    group.append(mat[row + 2][col + 2])

    return group

def checkArr(row):
    row.sort()
    count = 0
    for i in range(1,10):
        if(row[i-1] == i):
            count = count + 1
    return (count == 9)

def checkAll(mat, row, col):
    boolRow = checkArr(mat[row])
    boolCol = checkArr(getCol(mat, col))
    boolGroup = checkArr(getGroup(mat, row, col))
    return (boolRow and boolCol and boolGroup)

def validAll(mat, row, col):
    #print(mat[row])
    #print(getCol(mat, col))
    #print(getGroup(mat, row, col))
    boolRow = checkValid(mat[row], mat[row][col])
    boolCol = checkValid(getCol(mat, col),mat[row][col])
    boolGroup = checkValid(getGroup(mat, row, col),mat[row][col])
    return (boolRow and boolCol and boolGroup)

def printMatrix(mat):
    for i in mat:
        for j in i:
            print(j, end=",")
        print()
    print()

def solveTable2(mat, row = 0, col = 0):
    orgVal = mat[row][col]
    cmat = []
    for i in range(1, 10):
        mat[row][col] = i
        if validAll(mat, row, col):
            row = row + 1
            if(row == 9):
                row = 0
                col = (col + 1) % 9
            cmat = solveTable2(mat, row, col)
        
    return cmat

def solveTable(mat, row = 0, col = 0, depth = 0):
    print("Currect depth=",depth)
    cMat = mat[:]
    sRow = row
    sCol = col
    if mat[row][col] != 0:
        sRow = sRow + 1
        if(sRow == 9):
            sRow = 0
            sCol = (sCol + 1) % 9
        
        print("Solving using row=", sRow, "col=", sCol, "val=", mat[sRow][sCol])
        if sRow == 8 and sCol == 8:
            return mat
        else:
            mat = solveTable(mat, sRow, sCol, depth + 1)
    else:
        mat = cMat[:]
        for i in range (1, 10):
            mat[row][col] = i
            if(depth % 5 == 0):
                printMatrix(mat)
            if validAll(mat, row, col):
                sRow = sRow + 1
                if(sRow == 9):
                    sRow = 0
                    sCol = (sCol + 1) % 9
                print("Solving using row=", sRow, "col=", sCol, "val=", mat[sRow][sCol])
                if sRow == 8 and sCol == 8:
                    return mat
                else:
                    mat = solveTable(mat, sRow, sCol, depth + 1)
                    if(mat[row][col] > 0):
                        return mat
                    #return solveTable(table, sRow, sCol, depth + 1)
    cMat[sRow][sCol] = -1
    return cMat
    


table = [
        #0 1 2  3 4 5  6 7 8 
        [0,0,0, 0,0,0, 0,0,0], #0
        [0,1,2, 0,3,4, 5,6,7], #1
        [0,3,4, 5,0,6, 1,8,2], #2

        [0,0,1, 0,5,8, 2,0,6], #3
        [0,0,8, 6,0,0, 0,0,1], #4
        [0,2,0, 0,0,7, 0,5,0], #5

        [0,0,3, 7,0,5, 0,2,8], #6
        [0,8,0, 0,6,0, 7,0,0], #7
        [2,0,7, 0,8,3, 6,1,5]  #8
    ]


#print(validAll(table, 0, 0))
print(printMatrix(solveTable(table)))
#print(checkRow(table[2]))
