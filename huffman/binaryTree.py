class node:
    def __init__(self, val = 0, name = "", parent = None):
        self.left = None
        self.right = None
        self.name = name
        self.value = val
        self.parent = parent
        self.deepness = 0

    def test(self):
        print("test succesful")

    def addNode(self, nNode):
        if nNode.value < self.value:
            if not self.left:
                nNode.parent = self
                self.left = nNode
                self.value += nNode.value
                self.name += nNode.name
            else:
                self.left.addNode(nNode)
        else:
            if not self.right:
                nNode.parent = self
                self.right = nNode
                self.value += nNode.value
                self.name += " | "  + nNode.name
            else:
                self.right.addNode(nNode)

    def __str__(self):
        return self.name + "value: " + str(self.value)

def printTree(Tree, deepness = 0):
    if not Tree:
        return 
    printTree(Tree.left, deepness = deepness + 1)
    print("+" if deepness else "", "-" * deepness,"name: ", Tree.name, " value: ", Tree.value, sep="")
    printTree(Tree.right, deepness = deepness + 1)