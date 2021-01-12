from charCount import characterCount
from binaryTree import node, printTree

#TODO:
def minInsert(lst, val, key=None):
    for i, x in enumerate(lst):
        if i < len(lst) - 1:
            if key:
                if key(val) > key(x) and key(val) < key(lst[i + 1]):
                    lst.insert(i + 1, val)
                    return
            else:
                if val > x and val < lst[i + 1]:
                    lst.insert(i + 1, val)
                    return
        else:
            lst.append(val)
            return

def transverseTree(Tree, char, code=""):
    if Tree:
        if Tree.name == char:
            print(code)
            return code
        temp = transverseTree(Tree.left, char, code + "0")
        if not temp:
            temp = transverseTree(Tree.right, char, code + "1")
        return temp
    else:
        return None


filename = "encoded.txt"
file = open(filename, "r")

charDict = characterCount(file.read())
charList = [(x,charDict[x]) for x in charDict]
charList.sort(key=lambda xy : (xy[1], xy[0]))

#print(charList)
nodeList = []
nodeCount = 0


for lett, value in charList:
    nodeList.append(node(val=value, name=lett))


while len(nodeList) > 2:
    base = node()
    base.addNode(nodeList.pop(0))
    base.addNode(nodeList.pop(0))
    minInsert(nodeList, base, lambda x : x.value)


finalNode = node()

finalNode.left = min(nodeList, key=lambda x : x.value)
finalNode.right = max(nodeList, key=lambda x : x.value)

#printTree(finalNode)

codeDict = {}

for char in charDict:
    t = transverseTree(finalNode, char)
    print(t)
    codeDict[char] = t

print(codeDict)

file.close()