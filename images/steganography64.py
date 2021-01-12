from PIL import Image
import math
import sys

alphabet = "\0ABCEDFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\n"
alphadict = {c : i for i, c in enumerate(alphabet)}



write = False

if write:
    i = 0
    im = Image.open('parrot.jpg' if len(sys.argv) < 2 else sys.argv[1])
    pix = im.load()

    newImg = Image.new('RGB', im.size) #Can be changed to RGBA
    newPix = newImg.load()

    data = """4j4no8VGKcbVlqOGc11p
X8KZ4YLOSrtkzAQU7dRm
G285tY52j4Pb7p0YLUc5
7t1WeHVpjMte9csoseOA
hLZ7jHAacZDyC0220qqV
lR49FL9bNQQR9G5kgUlg
UyYZMunyi4JL9DwFBzQK
H498VRwkpnny0blZKgOu
HBijS7Fp82mdav66IykO
bq8jFrXQ6IKoAvbx42cx"""


    for w in range(0, im.size[0]):
        for h in range(0, im.size[1]):
            if i <= len(data):
                char = alphadict[data[i]] if i < len(data) else 0
                rbits = char & 0b000011
                gbits = (char & 0b001100) >> 2
                bbits = (char & 0b110000) >> 4
                r, g, b = pix[w,h]
                #print("rbg:", end="")
                #print(r,g,b, sep=" ")
                r = r & 0b11111100
                g = g & 0b11111100
                b = b & 0b11111100

                r = r | rbits
                g = g | gbits
                b = b | bbits
                newPix[w,h] = (r, g, b)
            else:
                newPix[w,h] = pix[w,h] 
            i = i + 1
    
    newImg.save("stegan.png")
else: #read
    im = Image.open('stegan.png' if len(sys.argv) < 2 else sys.argv[1])
    pix = im.load()

    readData = ""

    for w in range(0, im.size[0]):
        for h in range(0, im.size[1]):
            r, g, b = pix[w,h]
            r = r & 0b00000011
            g = g & 0b00000011
            b = b & 0b00000011
            charI = r | g << 2 | b << 4
            if charI == 0:
                print(readData)
                quit()
            else:
                char = alphabet[charI]
                readData = readData + char
