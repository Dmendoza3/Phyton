from PIL import Image
import sys
import os

write = False

if write:
    i = 0
    im = Image.open('blank4k.png' if len(sys.argv) < 2 else sys.argv[1]).convert('RGBA')
    pix = im.load()

    newImg = Image.new('RGBA', im.size)
    newPix = newImg.load()

    filename = "parrot4k.png"
    file = open(filename, "rb")
    dataSize = os.stat(filename).st_size
    print(dataSize)
    data = dataSize.to_bytes(4,"big") + file.read(dataSize)

    meta = 4
    
    for w in range(0, im.size[0]):
        for h in range(0, im.size[1]):
            if i <= dataSize:
                char = data[i] if i < dataSize else 0
                rbits = (char & 0b00000011)
                gbits = (char & 0b00001100) >> 2
                bbits = (char & 0b00110000) >> 4
                abits = (char & 0b11000000) >> 6
                r, g, b, a= pix[w,h]
                r = r & 0b11111100
                g = g & 0b11111100
                b = b & 0b11111100
                a = a & 0b11111100

                r = r | rbits
                g = g | gbits
                b = b | bbits
                a = a | abits
                newPix[w,h] = (r, g, b, a)    
            else:
                newPix[w,h] = pix[w,h] 

            i = i + 1
    
    newImg.save("stegan255.png")
else: #read
    im = Image.open('stegan255.png' if len(sys.argv) < 2 else sys.argv[1])
    pix = im.load()

    filename = "destegan.png"
    file = open(filename, "wb")

    readData = b''

    meta = 3
    filesize = 0
    print(im.size)
    for w in range(0, im.size[0]):
        for h in range(0, im.size[1]):
            r, g, b, a = pix[w,h]
            r = r & 0b00000011
            g = g & 0b00000011
            b = b & 0b00000011
            a = a & 0b00000011
            charI = r | g << 2 | b << 4 | a << 6
            if meta >= 0:
                filesize = filesize | charI << (meta * 8)
                meta = meta - 1
            else:
                if filesize > 0:
                    readData = readData + charI.to_bytes(1, "big")
                    filesize = filesize - 1
                    #if filesize % 1000 == 0:
                    #    print(filesize)
                else:
                    continue
    file.write(readData)
    file.close()