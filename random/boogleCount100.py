import random
i = 1
ite = 0
sample = 10000
for j in range(1, sample):
    i = 1
    while (True):
        ite = ite + 1
        rand = random.randint(0, 100)
        if i == rand:
            print(i)
            i = i + 1
        if i == 101:
            break

print(ite)
print("avg = ", ite / sample)