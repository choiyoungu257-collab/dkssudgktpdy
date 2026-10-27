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

e = np.zeros(7,dtype = int)
e[3] = 1
e[6] = 1
r.append((AN[2]+e)%2)


BN.append((H@r[0])%2)


print(r)
for b in range(7):
    if np.array_equal(H[:,b], BN[0]):
        r[0][b]= (r[0][b]+1)%2
print(AN[2])
print(BN)
HN.append((H@r[0])%2)
print(r)
print(HN)