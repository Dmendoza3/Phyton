#For loop
words = ['cat', 'window', 'defenestrate']
arrtp = [('a',1),('b',2),('c',3)]
for w in words:
    print(w, len(w))

#Allows to modify list not affecting the loop
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)

#Loop with numbers
for i in range(5,15):
    print(i)

#Loop with range, len
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

#List range
print(list(range(5)))

#Breaks
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else: #Else of a loop executes at end of range not after a break
        # loop fell through without finding a factor
        print(n, 'is a prime number')

#Continues
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)


for i, x in enumerate(words):
    print(x)

for x,y in arrtp:
    print(y)
