from PIL import Image
import math
import sys
import os


FileName = "bwparrot.jpg"
file = open(FileName, "rb")
filesize = os.stat(FileName).st_size

WIDTH = int(math.sqrt(filesize / 3) + 1)

newImg = Image.new('RGB', (WIDTH, WIDTH), color=(0, 0, 0)) #Can be changed to RGBA
newPix = newImg.load()

i = 0
for w in range(0, newImg.size[0]):
    for h in range(0, newImg.size[1]):
        if i < filesize - 3:
            b1, b2, b3 = file.read(3)
            newPix[h,w] = (b1, b2, b3)
        else:
            newPix[h,w] = (255, 0, 255)#if 'RGBA' : (0,0,0,0)
        i = i + 3

    

##im.show()
##im.save('hcparrot.jpg')
newImg.save("palette.png")