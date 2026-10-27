import numpy as np
from itertools import product


G = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,1,0,1],[1,0,1,1],[0,1,1,1]])
H = np.array([[1,1,0,1,1,0,0],[1,0,1,1,0,1,0],[0,1,1,1,0,0,1]])
AN = []
r = []
BN = []
HN = []
all =list(product([0,1], repeat=4))

for b in all:
    b_vector = np.array(b)
    AN.append((G@b_vector)%2)

for n in range(7):
    e = np.zeros(7, dtype = int)
    e[n]=1
    for j in AN:
        r.append((j + e) %2)

for i in range(112):
    BN.append((H@r[i])%2)

for a in range(112):
    for b in range(7):
        if np.array_equal(H[:,b], BN[a]):
            r[a][b]= (r[a][b]+1)%2
            break
print(BN)
for i in range(112):
    HN.append((H@r[i])%2)
print(HN)