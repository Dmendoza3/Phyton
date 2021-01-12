from PIL import Image
import random

size = (1600,1600)
newImg = Image.new('RGB', size)
newPix = newImg.load()

for w in range(0, newImg.size[0]):
    for h in range(0, newImg.size[1]):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        #a = 255#random.randint(0, 255)
        newPix[w,h] = (r, g, b)#, a)

newImg.save("random.png")