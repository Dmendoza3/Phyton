import math

st = input()
st = st.split(",")
Q = []
C = 50
H = 30
for i in st:
    D = int(i)
    Q.append(math.sqrt(((2 * C * D) / H)))

print(Q)