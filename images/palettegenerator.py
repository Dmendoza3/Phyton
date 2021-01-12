from PIL import Image
import math
import sys
import colorsys

def call(x):
    return (x[2], x[0], x[1])

def valRGB(x):
    return math.sqrt(x[0] ** 2 + x[1] ** 2 + x[2]**2)

def step (r,g,b, repetitions=1):
    lum = math.sqrt( .241 * r + .691 * g + .068 * b )

    h, s, v = colorsys.rgb_to_hsv(r,g,b)

    h2 = int(h * repetitions)
    lum2 = int(lum * repetitions)
    v2 = int(v * repetitions)

    if h2 % 2 == 1:
        v2 = repetitions - v2
        lum = repetitions - lum

    return (h2, lum, v2)


def lum (r,g,b):
	return math.sqrt( .241 * r + .691 * g + .068 * b )

im = Image.open('random.png' if len(sys.argv) < 2 else sys.argv[1])
pix = im.load()

colorDict = {}

for w in range(0, im.size[0]):
    for h in range(0, im.size[1]):
        colorDict[pix[w,h]] = 0

print(len(colorDict))

WIDTH = int(math.sqrt(len(colorDict)) + 1)
newImg = Image.new('RGB', (WIDTH, WIDTH), color=(255, 255, 255)) #Can be changed to RGBA
newPix = newImg.load()

colorLst = list(colorDict.keys())


#colorLst.sort(key=lambda rgb: colorsys.rgb_to_hsv(*rgb) )
colorLst.sort(key=lambda rgb: lum(*rgb)	) #luminosity sorting
#colorLst.sort(key=lambda (r,g,b): step(r,g,b,8)	)
#colorLst.sort(key=valRGB)

#TODO:sort colors
#   save in dict the hex of color as key then sort keys 

i = 0
for w in range(0, newImg.size[0]):
    for h in range(0, newImg.size[1]):
        if i < len(colorLst):
            newPix[h,w] = colorLst[i]
        else:
            newPix[h,w] = (255, 0, 255)#if 'RGBA' : (0,0,0,0)
        i = i + 1

    

##im.show()
##im.save('hcparrot.jpg')
newImg.save("palette.png")