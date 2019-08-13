import random

arr = [5,2,4,1,6,7,3]
arrOrd = arr.sort()
while True:
    rand = random.randint(0, len(arr))
    x = arr[-1]
    arr[-1] = arr[rand]
    arr[rand] = x
    if arr == arrOrd:
        break