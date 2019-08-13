import xml.etree.ElementTree as ET

def profPrint(parent, x = 0):
    for child in parent:
        #print("\t" * x, end = '', file=outFile)
        #print(child.tag, end = ': ')
        #print("\t" * x, end = '')
        print(child.text, end = ' ', file=outFile)
        #print("\t" * x, end = '')
        #print(child.text, file=outFile)
        profPrint(child, x + 1)

outF = "./rawtext.txt"
outFile = open(outF, "w")

tree = ET.parse('1000000.xml')
root = tree.getroot()
profPrint(root)
