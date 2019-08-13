from PIL import Image

arr = [0,0,0]
im = Image.open('parrot.jpg')
pix = im.load()
cleanImg = im.load()

#turn black and white
for w in range(0, im.size[0]):
    for h in range(0, im.size[1]):
        avgcol = int(sum(pix[w,h]) / 3)
        pix[w,h] = (avgcol, avgcol, avgcol)

im.save('bwparrot.jpg')

for w in range(0, im.size[0]):
    for h in range(0, im.size[1]):
        arr[0] = arr[0] + pix[w,h][0]
        arr[1] = arr[1] + pix[w,h][1]
        arr[2] = arr[2] + pix[w,h][2]

arr[0] = arr[0] / (w * h)
arr[1] = arr[1] / (w * h)
arr[2] = arr[2] / (w * h)


newcol = (int(arr[0]), int(arr[1]), int(arr[2]))
#for w in range(0, im.size[0]):
#    for h in range(0, im.size[1]):
#        pix[w,h] = newcol

#im.show()
print(newcol)

midcolor = sum(newcol) / 3
print(midcolor)

for w in range(0, im.size[0]):
    for h in range(0, im.size[1]):
        avgcol = int(sum(pix[w,h]) / 3)
        #print(str(avgcol) + ":" + str(midcolor))
        if avgcol < midcolor:
            pix[w,h] = (0, 0, 0)
        else:
            pix[w,h] = (255, 255, 255)

for w in range(0, im.size[0]):
    for h in range(0, im.size[1]):
        if pix[w + 1, h] 
#im.show()
im.save('hcparrot.jpg')
