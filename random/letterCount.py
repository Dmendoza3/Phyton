import sys

filename = sys.argv[1]

inF = open(filename, 'r')
outF = open("result.csv", 'w')

alphastr = "abcdefghijklmnopqrstuvwxyz"

alpha = {}

for x in alphastr:
    alpha[x] = 0

letter = inF.read(1)
inF.seek(0)
while letter:
    letter = inF.read(1).lower()
    if alphastr.find(letter) != -1 and letter != ' ' and letter != '':
        alpha[letter] = alpha[letter] + 1

for key in alpha:
    print(key + ";" + str(alpha[key]), file=outF)


