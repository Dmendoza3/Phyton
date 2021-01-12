x = 344444444

b0,b1,b2,b3 = [c for c in x.to_bytes(4,"big")]

y = b0 << 24 | b1 << 16 | b2 << 8 | b3 << 0

print(b0,b1,b2,b3)
print(y)