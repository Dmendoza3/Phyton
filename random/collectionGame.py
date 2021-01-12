import random

rarities = ['common', 'uncommon', 'rare', '']

collection = {}
collectionRate = {}

collected = []

def generateCollection(num, nRarities=3, rate=0.75):
    cardsLeft = num
    for r in range(nRarities):
        if r < nRarities - 1: 
            nPerRarity = int(cardsLeft * rate)
        else:
            nPerRarity = cardsLeft

        collection[(nPerRarity)] = []
        for n in range(nPerRarity):
            collection[nPerRarity].append('name'  + str(nPerRarity) + str(random.randint(100, 999)))

        cardsLeft -= nPerRarity

    prevN = 0
    for x in collection:
        collectionRate[(prevN + 1, prevN + x)] = x
        prevN += x 

def getCard():
    rand = random.randint(1, 100)

    for x in collectionRate:
        if rand in range(x[0], x[1]):
            print(collectionRate[x])
            return random.choice(collection[collectionRate[x]])


generateCollection(100)

print(collection)
for x in range(10):
    print(getCard())

